---
title: "Crypto Narratives by Direction — Master Index"
type: index
created: 2026-06-04
updated: 2026-06-04
status: draft
tags: [crypto, narrative-impact, market-regime, backtesting, index]
aliases: ["Narratives by Direction", "Bullish Bearish Neutral Narratives"]
related: ["[[crypto-narratives-overview]]"]
---

> **Auto-generated** from `catalog/all-narratives.json` by `tools/generate_narratives_by_direction.py`. Do not hand-edit — regenerate after `build_narrative_catalog.py`.

The master directory of every price-moving crypto narrative in the catalog, grouped by direction. **Part A** lists the *narrative types* (archetypes — repeatable patterns) by their unconditional bias. **Part B** is the full *event list* — every historical instance grouped by the direction it actually moved price. Bias is a historical tilt, not a law: most narratives are regime-conditional (e.g. ETF launches are structurally bullish but 'sell-the-news' on the day). See [[crypto-narratives-overview]] and each category page for mechanisms, leading signals, and backtest features.

**Totals:** 19 categories · 69 narrative archetypes · 290 historical instances. Archetypes by bias: 🟢 22 bullish · 🔴 33 bearish · ⚪ 13 mixed · ⚫ 1 neutral. Events by realized move: 🟢 99 up · 🔴 157 down · ⚪ 34 flat/no-isolable.

## Part A — Narrative types (archetypes) by bias

### 🟢 Bullish narrative types (22)

| Narrative archetype | Category | Typical magnitude | Mechanism (who's on the other side) | n |
|---|---|---|---|--:|
| **Flagship AI-Agent Token Launch Pump (reflexive parabola)** | [[ai-agent-tokens]] | +500% to +8000% on the launch token over its first 1-4 weeks; co-movement +20% to +100% on sector peers | A novel AI-agent token launches via fair-launch/launchpad (pump.fun, Virtuals bonding curve) with a viral story (an autonomous AI, an a16z-themed DAO, a Marc Andreessen… | 4 |
| **Launchpad Graduation Pumps & AI-Infra Token Consolidation** | [[ai-agent-tokens]] | Agent graduation: token +50% to +1000% on listing; VIRTUAL +10% to +30% on graduation waves; merger: +50% to +300% on announcement (FET ATH ~$3.47) | Two structural sub-patterns. (a) Launchpad graduation: on Virtuals, an agent's bonding curve filling 42,000 VIRTUAL triggers a Uniswap listing - a deterministic supply/liquidity… | 3 |
| **Post-Halving Bull Cycle (the 12-18 month parabolic run)** | [[bitcoin-halving-narrative]] | halving-day-to-peak: ~+9000% (2012), ~+2900% (2016), ~+700% (2020), ~+95% (2024) — diminishing each cycle | The halving cuts new BTC issuance in half overnight (50->25->12.5->6.25->3.125 BTC/block). Daily new supply that miners must sell to cover costs drops sharply, while demand is… | 4 |
| **Pre-Halving Rally / Buy-the-Rumor** | [[bitcoin-halving-narrative]] | roughly +100% to +180% in the ~12 months leading into the halving | In the 6-12 months ahead of a halving, the upcoming supply cut is a well-telegraphed, calendar-certain event. Traders and investors front-run the expected post-halving scarcity… | 2 |
| **Sustained Accumulation / mNAV-Premium Flywheel (ongoing buys funded at a premium)** | [[corporate-treasury]] | individually negligible (<1-2% per buy); cohort contributes meaningfully to multi-month uptrends | Once established, a treasury company runs a reflexive flywheel: because its stock trades at a premium to the crypto it holds (mNAV > 1), it issues equity/convertibles/preferreds… | 5 |
| **Treasury-Adoption Announcement (company pivots to crypto reserve)** | [[corporate-treasury]] | +20% to +4000%+ on the announcing stock (size-dependent); BTC/ETH typically -2% to +3% same day | A public company announces it is adopting BTC/ETH as a primary treasury reserve asset, usually copying the MicroStrategy playbook. The other side of the trade is equity investors… | 8 |
| **Narrative ignition / TVL land-grab (yield-farming, restaking points, RWA hype)** | [[defi-narratives]] | +100% to +1,000%+ on flagship tokens during ignition; outlier fair-launch tokens (YFI) >100,000% | A novel yield mechanism (liquidity mining 2020, restaking points 2023-24, tokenized treasuries 2024) creates a reflexive loop: emissions/points subsidize deposits, TVL spikes, the… | 7 |
| **Challenger / 'Next Ethereum-Killer' Revival Rotation** | [[l1-l2-rotation]] | +200% to +1100% on the challenger over a rotation leg; relative outperformance vs ETH of 30-90% on the ratio | Capital rotates out of the incumbent leader (usually ETH) into a faster/cheaper challenger L1 that has a fresh catalyst - a killer app, a usage milestone, or a recovery from a… | 4 |
| **Incentive-Driven Ecosystem Pump (and Fade)** | [[l1-l2-rotation]] | +200% to +1500% on the L1 token during the incentive window; -70% to -95% on the subsequent unwind | A chain foundation deploys a large liquidity-mining / DeFi incentive program (e.g. Avalanche Rush $180M, BSC's accelerator funds) that subsidizes yield far above competing chains.… | 3 |
| **Banking/Fiat Stress Flight-to-Bitcoin** | [[macro-events]] | BTC +15% to +30% over the stress window | When the stress is in the traditional banking/fiat system itself (bank runs, stablecoin-reserve scares, sovereign-currency wobble) rather than a generic risk-off, Bitcoin can… | 3 |
| **Macro Liquidity / Risk-On Tailwind** | [[macro-events]] | BTC +3% to +12% on the print; multi-week regime moves +20% to +60% | When the market prices easier policy (a dovish Fed surprise, a rate CUT, a cooler-than-expected CPI, a falling DXY, expanding M2/global liquidity), the discount rate on… | 3 |
| **Celebrity / Influencer Pump on an Existing Memecoin** | [[memecoin-mania]] | +20% to +600% on the named coin into the catalyst; -20% to -40% sell-the-news reversal within 24-48h | A high-follower individual (Elon Musk, Mark Cuban) tweets or publicly endorses an existing memecoin (DOGE, SHIB). Retail FOMO buyers chase the spike on near-zero float depth,… | 5 |
| **Launch-Pump-and-Hold (Fair-Launch / Revenue-Backed)** | [[platform-launches]] | +50% to +700% on the named coin within weeks of launch | The rare inverse of sell-the-news. When a token launches with (a) NO VC/private-investor allocation to dump, (b) a product with real, demonstrable revenue/usage, and (c) supply… | 5 |
| **Revenue-funded buyback flywheel (usage -> token demand)** | [[platform-launches]] | can drive multi-month outperformance/decoupling (HYPE +82.9% in May 2026 to an ATH while majors fell); magnitude tracks fee revenue | A protocol routes the bulk of its trading-fee revenue into continuous open-market buybacks of its own token, turning exchange usage directly into automatic, price-insensitive… | 2 |
| **Idiosyncratic regulatory de-risking of a named coin** | [[regulatory-approvals-policy]] | +20% to +30%+ on the named coin in 24-72h, often with low BTC correlation | A regulatory overhang specific to one asset is lifted or expected to lift — a hostile regulator departs, a lawsuit settles, an asset is endorsed, or an accounting penalty is… | 3 |
| **Legislative framework passage (stablecoin / market-structure)** | [[regulatory-approvals-policy]] | Sector/ETH +20% to +30% while BTC roughly flat to +5% | Passage (or near-passage) of a sweeping crypto law clarifies which assets fall under SEC vs CFTC and legitimizes a sub-sector (stablecoins, settlement layers). The re-rating… | 6 |
| **Pro-crypto policy regime shift (election / executive pivot)** | [[regulatory-approvals-policy]] | BTC +25% to +55% over 1-6 weeks; high-beta alts +50% to +150%+ | A genuine, hard-to-fully-anticipate shift in the regulatory regime — a pro-crypto candidate winning, or an executive order signaling state endorsement — reprices the entire asset… | 3 |
| **Regulated domestic access / new-product expansion** | [[regulatory-approvals-policy]] | no clean spot move on the event; structural depth/liquidity gain | A regulator clears a new onshore product or venue (perpetual futures, leverage, new derivatives, prediction-market preemption) that widens domestic access, market depth, and… | 2 |
| **Sovereign / state strategic-reserve accumulation** | [[regulatory-approvals-policy]] | per-event not isolable (<~3%, lost in market noise); structurally bullish only with sustained large sovereign buying | A government (federal or US state) signals or executes strategic Bitcoin accumulation. Announcements and enabling bills are sentiment events; actual purchases create real demand.… | 3 |
| **Deregulation / Crackdown Reversal (the inverse, 2024-2026)** | [[regulatory-bans]] | named token +40% to +100%+ on full relief (e.g. TORN ~+60% on the day); broad sentiment tailwind | The mirror image of the crackdown archetype: when a previously-imposed ban, sanction, or lawsuit is lifted or dropped, the overhang that suppressed a token clears and price… | 2 |
| **Low SSR / Loaded Exchange Reserves (Positioning Indicator)** | [[stablecoin-supply]] | historically preceded multi-month BTC rebounds of tens of percent when accompanied by genuine stablecoin accumulation | The Stablecoin Supply Ratio (SSR = BTC market cap / stablecoin market cap) measures how much BTC the existing stablecoin pile could buy. A low SSR means stablecoins have outsized… | 3 |
| **Net Mint Expansion (Dry-Powder Injection)** | [[stablecoin-supply]] | +0.4% to +2.5% on BTC within hours of a discrete >=$1B mint; +10% to +300% on BTC over multi-month sustained supply-expansion regimes | Tether and Circle mint new stablecoins on-demand when authorized resellers and exchanges wire in USD (or pre-mint inventory in anticipation of demand). Newly issued USDT/USDC… | 6 |

### 🔴 Bearish narrative types (33)

| Narrative archetype | Category | Typical magnitude | Mechanism (who's on the other side) | n |
|---|---|---|---|--:|
| **AI-Sector Rotation + Reflexive Crash (correlated cohort unwind)** | [[ai-agent-tokens]] | -60% to -90% peak-to-trough on individual AI-agent tokens within ~6 weeks; sector mcap fell roughly -65% to -70% (from ~$17B-$20B toward $5B-$7B) | AI-agent tokens trade as a single high-beta narrative basket. Capital rotates in together on hype and out together on shock. On the way up, latecomers buy the basket as a theme;… | 4 |
| **Alt-season extreme as a late-cycle top signal** | [[bitcoin-dominance-rotation]] | post-peak alt baskets routinely draw down 70-90%+; BTC.D rebounds 15-30pp off the bottom | An alt-season is the last leg of the crypto risk curve: once BTC and ETH have run, the most speculative capital chases low-quality alts and memecoins. Historically the dominance… | 2 |
| **Post-Cycle Bear Market (the deflationary back half of the 4-year cycle)** | [[bitcoin-halving-narrative]] | -70% to -85% peak-to-trough | After the post-halving bull tops out (~12-18 months post-halving), the reflexive process runs in reverse. Late buyers who entered on leverage near the top are underwater; as price… | 4 |
| **Distribution / Forced Selling / mNAV-Discount Unwind (the flywheel in reverse)** | [[corporate-treasury]] | -2% to -5% coin on a single disclosed corporate sale; -10% to -25% coin during a full premium-collapse/forced-selling regime | The reflexive flywheel runs backward. When the coin falls and the stock's premium collapses to or below net asset value (mNAV <= 1), accretive equity issuance stops, and pressure… | 7 |
| **DeFi reflexive deleveraging / contagion (exploits, founder-collateral, yield unwind)** | [[defi-narratives]] | -10% to -25% on the directly affected token in 24h; -5% to -15% sector contagion | DeFi yields are often built on leverage and recursive collateral (looping, LST/LRT leverage, founder borrows against governance token). A shock — an exploit, a depeg, or a yield… | 3 |
| **Points/airdrop 'sell the news' (TGE distribution dump)** | [[defi-narratives]] | -30% to -85% from listing/ATH within weeks for typical farm-and-dump tokens | Farmers accumulate points/eligibility expecting an airdrop. At the token-generation event (TGE) / claim, recipients who farmed for free have ~100% cost basis as profit and dump… | 5 |
| **Acute Insolvency / Bank-Run Freeze** | [[exchange-collapses]] | Platform token: -70% to -95% in 24-72h. BTC: -8% to -20% over the acute window. Closely-tied ecosystem coins: -40% to -60%. | A platform reveals (or is revealed) to be insolvent and freezes withdrawals. Depositors who believed their balance was money they could withdraw on demand discover the platform… | 4 |
| **Contagion Cascade / Counterparty Domino** | [[exchange-collapses]] | BTC: -50% to -65% peak-to-trough over the full cascade. ETH and large alts: -70% to -80%. The compounding of multiple shocks, not any single one, drives the depth. | Crypto lenders and funds form a tightly interconnected credit web — the same collateral (often a token like LUNA, GBTC, or stETH) is rehypothecated across multiple desks. When one… | 4 |
| **Estate Distribution / Repayment Supply Overhang** | [[exchange-collapses]] | BTC: roughly -5% to -8% on a given trigger (e.g. the July 2024 ~-6% 24h move); rarely the primary cause of a deep crash, more a drag/resistance. | Years after an exchange collapses, the bankruptcy estate recovers a large stash of coins and is scheduled to return them to creditors. Because many creditors bought claims cheaply… | 2 |
| **Centralized exchange hack (market-wide sentiment shock, mean-reverting)** | [[hacks-exploits]] | -2% to -6% BTC/ETH same-day; larger drawdowns into following days when a hack compounds an already risk-off macro tape, much of it retraced | A large CEX has its hot/cold wallets drained. Unlike a protocol token crash, there is usually no single 'victim token' to short — the exchange typically socializes the loss… | 3 |
| **Cross-chain bridge exploit (ecosystem L1/token drag-down)** | [[hacks-exploits]] | -10% to -25% on the ecosystem token within 24-48h | A bridge holds large pooled collateral and is a fat single point of failure. When it's drained (validator compromise, signature/mint forgery), the loss is huge in absolute terms… | 6 |
| **DeFi protocol exploit (governance/native token crash)** | [[hacks-exploits]] | -15% to -45% on the hacked protocol's token within 24-72h | A smart-contract bug (flash loan, reentrancy, oracle/logic flaw) lets an attacker drain a protocol's TVL. The protocol's own governance/native token is the most direct casualty:… | 8 |
| **Rotation Unwind / Challenger Ratio Mean-Reversion** | [[l1-l2-rotation]] | -40% to -90% on the challenger; challenger/ETH ratio reverts 25-50%+ off its high | The mirror image of the revival rotation. After a challenger L1 has massively outperformed (ratio vs ETH at extremes, narrative saturated, media calling a 'flippening'), the… | 5 |
| **Crypto Leverage Liquidation Cascade (macro-triggered)** | [[macro-events]] | BTC -10% to -16% intraday; alts -25% to -50% intraday wicks | A macro headline pierces a market that is structurally over-leveraged (high perp open interest, positive funding, crowded longs). The initial drop hits liquidation prices,… | 3 |
| **Macro Risk-Off Liquidity Shock** | [[macro-events]] | BTC -8% to -20% peak-to-trough; alts -20% to -45% | An exogenous macro shock (surprise hawkish Fed, hot CPI, tariff escalation, global VIX spike) forces a synchronized de-risking across all risk assets. Crypto sits at the far end… | 6 |
| **Launch-Day Parabolic Token (Politician / Pump.fun / Celebrity Coin)** | [[memecoin-mania]] | +1000% to +10000% in the first hours, then -80% to -98% from peak within weeks | A brand-new token launches with almost all supply held by insiders/team and a thin public float. A loud endorsement or hype event (a politician's own announcement, a celebrity, or… | 5 |
| **Memecoin Season as a Late-Cycle Risk-On Top Signal** | [[memecoin-mania]] | memecoin sector market cap -75% to -80% from cycle peak; broad market correction of -20% to -50%+ | When speculative capital rotates down the risk curve into the lowest-quality assets (memecoins), it signals that the marginal buyer is exhausted and dry powder is being spent on… | 5 |
| **Pre-IPO / synthetic-asset perp oracle-failure flash crash** | [[platform-launches]] | -45% to -80% in minutes on the affected contract; underlying platform token typically unaffected | New on-chain perp venues list contracts on illiquid, no-public-benchmark underlyings (pre-IPO names, synthetic equities) priced by a single third-party oracle. When the oracle… | 1 |
| **TGE / Airdrop Sell-the-News Dump** | [[platform-launches]] | -20% to -60% on the named coin from open within 1-7 days; -50% to -90% peak-to-trough over weeks | On the launch day a large slice of supply (typically 7-20% of total) lands in the wallets of airdrop recipients and points farmers who paid little or nothing for it. Their cost… | 11 |
| **National Tax / Access Throttling (India / Nigeria model)** | [[regulatory-bans]] | local exchange volume -70% to -82% (India TDS); local price gap ~-13-17% intraday on announcement; global BTC ~0% | A government doesn't ban crypto outright but throttles it via punitive taxes (India's 30% gains tax + 1% transaction TDS) or by cutting off banking/internet access to exchanges… | 3 |
| **Sovereign Trading / Mining Ban (China model)** | [[regulatory-bans]] | BTC -8% to -16% in 24h; -30% to -55% peak-to-trough over a multi-week crackdown wave | A large nation-state (overwhelmingly China, which at peak hosted >50% of BTC hashrate and a huge share of trading volume) bans banks from servicing crypto, bans exchanges, or bans… | 6 |
| **US Securities Enforcement (SEC vs token / exchange)** | [[regulatory-bans]] | named token -15% to -25% (alt-L1s) up to -50% to -73% (XRP, due to broad delisting); BTC roughly flat to -7% | The SEC (acutely in the Gensler era) sues an issuer or exchange and names specific tokens as unregistered securities. The mechanism is delisting-driven, not network-driven:… | 3 |
| **Converted legacy trust structural outflow (GBTC / ETHE)** | [[spot-etf-flows]] | contributed -15% to -20% peak-to-trough on BTC over the Jan-Feb 2024 episode; effect fades as outflows slow | When a high-fee closed-end trust (GBTC at 1.5%, ETHE at 2.5%) converts to an open-ended ETF, two mechanical sell forces fire: (1) arbitrageurs who bought the trust at a deep… | 2 |
| **Spot ETF launch day / approval 'sell the news'** | [[spot-etf-flows]] | -7% to -20% on the launching asset over 1-2 weeks | A spot ETF launch is a heavily pre-announced, date-certain catalyst. Traders accumulate spot in the weeks before, pricing in the expected demand. On the actual launch the catalyst… | 5 |
| **Algorithmic / reflexive death-spiral depeg** | [[stablecoin-depegs]] | -50% to -100% on the stablecoin; -95% to -100% on the sister token | An uncollateralized or under-collateralized stablecoin maintains its peg via an arbitrage loop that mints/burns a sister governance/seigniorage token (LUNA for UST, TITAN for… | 4 |
| **Net Burn / Redemption Contraction** | [[stablecoin-supply]] | contraction confirms ongoing drawdowns; standalone signal, hard to isolate, but accompanied BTC drawdowns of -30% to -70% in 2022 | When holders redeem stablecoins for USD, issuers burn the coins and supply contracts. Shrinking supply means dollars are leaving the crypto ecosystem (or being parked… | 2 |
| **Stablecoin Depeg Shock (Backing-Doubt)** | [[stablecoin-supply]] | depegged coin -3% to -100%; BTC/ETH -8% to -16% in the acute window, with sharp V-recoveries when backing is confirmed | When the market loses confidence that a stablecoin is fully backed (reserves stuck at a failed bank, opaque attestations, or an algorithmic peg breaking), the coin trades below… | 3 |
| **Open-interest washout / forced-liquidation cascade** | [[technical-signals]] | BTC -8% to -30% in 24h; alts/high-beta -15% to -50%; bounce of +5% to +15% within days | When perpetual-futures open interest and leverage build up (often alongside elevated funding), a sharp price move triggers margin calls. Exchange liquidation engines market-sell… | 4 |
| **Cliff Unlock (large discrete insider release)** | [[token-unlocks-narrative]] | -10% to -25% on the named token over the surrounding window; extreme launch/megacliff cases (ICP) -80%+ over weeks | A vesting cliff releases a large discrete tranche of previously-locked tokens (team, investors, treasury) on a single date. Early investors who bought at seed/private valuations a… | 7 |
| **Continuous / Linear Vesting Emission** | [[token-unlocks-narrative]] | -2% to -10% per individual monthly unlock window; chronic relative underperformance vs sector over the vesting period | After the initial cliff, most tokens vest linearly (daily/weekly/monthly) over 2-4 years. Each tranche adds a steady stream of new sellable supply. Because the schedule is fully… | 5 |
| **Exchange Netflow / Whale Deposit Signal (continuous flow)** | [[whale-onchain-flows]] | -2% to -8% on BTC for large confirmed inflow spikes; stablecoin-inflow follow-through is direction-uncertain (claimed +3% to +10%, but observed cases include BTC declines) | Coins in self-custody cannot be sold on a CEX order book, so a spike in exchange inflows (especially concentrated in the top-10 deposits — the 'whale ratio') front-runs… | 5 |
| **Government / Seized-BTC Distribution (sovereign overhang)** | [[whale-onchain-flows]] | flat (transfer-only, no sale) to -17% peak-to-trough over a multi-week active liquidation campaign | Governments that seize BTC (Germany/Movie2k, US/Silk Road) are non-economic, price-insensitive sellers liquidating for fiat/legal reasons, not profit. They move large tranches to… | 5 |
| **Mt Gox / Estate Creditor Repayment Overhang** | [[whale-onchain-flows]] | -5% to -8% on BTC around major transfer/repayment dates; sharper on BCH | The Mt Gox rehabilitation trustee held ~142,000 BTC owed to creditors since the 2014 collapse. Because creditors sit on enormous unrealized gains (cost basis near zero) and coins… | 3 |

### ⚪ Mixed / regime-conditional narrative types (13)

| Narrative archetype | Category | Typical magnitude | Mechanism (who's on the other side) | n |
|---|---|---|---|--:|
| **Idiosyncratic Agent/Protocol Events (hacks, subnet launches, dTAO)** | [[ai-agent-tokens]] | Hack: -15% to -22% single-name in 24h; subnet alpha launch: initial spike then -30% to -70% dip; TAO sector beta | Single-name catalysts specific to an agent or protocol. (a) Agent compromise/hack: an autonomous agent's wallet or dashboard is exploited, breaking the 'autonomous AI' trust… | 4 |
| **BTC dominance regime (risk-on/off rotation within crypto)** | [[bitcoin-dominance-rotation]] | BTC.D swings of 15-35 percentage points across a full cycle; alt baskets can out/under-perform BTC by 50-200%+ over a rotation | Crypto capital rotates along a risk curve anchored by Bitcoin. In early-bull and risk-off phases, money concentrates in BTC (the 'reserve asset' of crypto) and dominance rises;… | 3 |
| **Vote-bribe / liquidity wars (Curve wars, veTokenomics)** | [[defi-narratives]] | several hundred to ~+2,000%+ on the meta-governance token during the war (range depends on launch reference price); then -90%+ structural decline | veTokenomics let token-lockers direct emissions to pools. Protocols needing deep liquidity bribe lockers to vote for their pool, creating demand for the emission-control token… | 2 |
| **L2 / New-Chain Token Launch & Airdrop Rotation** | [[l1-l2-rotation]] | wide launch-day price discovery; first-month follow-on rallies of +20% to +30% in single sessions, then multi-month -50%+ bleed | A Layer-2 or new chain that ran without a token (Arbitrum, Optimism, Base, Solana-era pre-token chains) launches or airdrops its governance token. Pre-launch, mercenary 'airdrop… | 5 |
| **Points-Farming Meta - Pre-Launch Inflow & Post-Airdrop Outflow** | [[platform-launches]] | protocol TVL/activity swings of -30% to -70% post-snapshot; ecosystem-token effect small unless airdrop is large | Before a TGE, protocols run 'points' programs that promise a future airdrop weighted by deposits/usage. This pulls in mercenary capital: TVL, deposits, fees, and on-chain activity… | 5 |
| **Pre-priced approval 'sell-the-news' then structural re-rating** | [[regulatory-approvals-policy]] | -14% to -19% drawdown on the named asset in the 2 weeks post-approval; +50% to +150% over the following 6-12 months | A long-telegraphed regulatory approval of an investment vehicle (spot ETF) gets priced in during the rumor/anticipation phase. On the actual approval, event-driven traders and… | 2 |
| **Sustained daily net inflows (bullish) / net outflows (bearish)** | [[spot-etf-flows]] | inflow streaks: +8% to +50% over the run; outflow streaks: -3% to -20% over the run | Spot ETFs are a structural marginal buyer: every dollar of net inflow forces the authorized participant to buy spot BTC/ETH for creation, and every dollar of net outflow forces a… | 9 |
| **Fiat/asset-backed reserve-shock depeg** | [[stablecoin-depegs]] | -9% to -25% for credible fiat-backed (recovers); ~-49% for impaired RWA-backed (permanent) | A collateralized stablecoin (USDC, USDR, FDUSD) loses peg because the market doubts the reserves are fully redeemable — a real impairment (USDC's $3.3B stuck at failed SVB; USDR's… | 4 |
| **Funding-rate / leverage-sentiment extreme (contrarian)** | [[technical-signals]] | fading sustained extreme-positive funding historically preceded -20% to -50% cycle corrections; buying deeply-negative funding preceded +30% to +600% recoveries | Perpetual funding is paid from the crowded side to the other side. Extreme positive funding (e.g. 0.2-0.3% per 8h sustained for weeks) means longs are paying heavily to stay long… | 4 |
| **Moving-average regime cross (golden/death cross, 200-DMA loss/reclaim)** | [[technical-signals]] | 200-DMA loss often accompanies a -10% to -25% drawdown already in progress; reclaim tends to precede +15% to +40% over 1-3 months | The 50/200-day cross and the 200-day MA are lagging trend filters. They do not cause moves; they confirm a regime that price already entered. The 'other side' is… | 5 |
| **On-chain valuation extreme (MVRV Z-score, realized price, NUPL, Pi-cycle)** | [[technical-signals]] | buying sub-1.0 MVRV historically returned triple-digit % within 12 months; selling MVRV-Z>7 avoided 50-80% cycle drawdowns | These metrics compare market price to aggregate cost basis (realized value). MVRV Z-score, realized price, NUPL and the Pi-cycle top indicator all measure how far price has… | 5 |
| **Estate / Bankruptcy Locked-Token Distribution** | [[token-unlocks-narrative]] | Highly variable: muted-to-modestly-negative on the sale-announcement (SOL ~-6% in 24h on the April 2024 sale, amid broader weakness), vs muted-to-flat on the eventual unlock; downside mainly via anticipation | A bankruptcy estate (FTX/Alameda) or large institutional holder controls a huge stack of LOCKED tokens it cannot freely sell. It monetizes them via discounted OTC/private auctions… | 4 |
| **Dormant / Satoshi-Era Wallet Awakening** | [[whale-onchain-flows]] | -1% to -3% knee-jerk dip on benign/non-exchange moves; larger drawdowns if confirmed exchange/OTC-bound, but increasingly absorbed (net flat) | Wallets dormant 10-14+ years (Satoshi-era 2010-2011 coins) suddenly moving generate intense speculation about a giant holder cashing out — the ultimate latent supply overhang… | 4 |

### ⚫ Neutral narrative types (1)

| Narrative archetype | Category | Typical magnitude | Mechanism (who's on the other side) | n |
|---|---|---|---|--:|
| **Venue-specific liquidity-cascade flash depeg** | [[stablecoin-depegs]] | -1% to -35% on the affected venue only; ~0% on aggregate/redeemable price | A well-collateralized stablecoin briefly prints a sharp discount on ONE venue (a single exchange order book or an imbalanced AMM pool) because of a localized liquidity vacuum —… | 3 |

## Part B — The event list (every instance, by realized direction)

### 🟢 Bullish events (price moved UP) — 99

| Date | Narrative / event | Asset | Impact | Window | Conf | Category |
|---|---|---|---|---|---|---|
| 2026-06-02 | HYPE hits an ATH ~$75.51 (Jun 2 2026), decoupling UPWARD while BTC/ETH/SOL crash - driven by the Assistance… | HYPE | +82.89% | May 2026 ($39.67 -> $72.55) | high | [[platform-launches]] |
| 2026-06-01 | Strategy (MSTR) reaches 843,706 BTC — ~3/4 of all corporate-held BTC; nearing its 1M target. | BTC | structural demand (no clean single-day move) | ongoing through 2026-06-01 | high | [[corporate-treasury]] |
| 2026-05-31 | Bitmine Immersion (BMNR) reaches 5,416,901 ETH (~4.49% of supply) - the largest corporate ETH treasury (MSTR… | ETH | structural demand (no clean single-day move; ETH fell ~40% YTD regardless) | H1 2026 accumulation | high | [[corporate-treasury]] |
| 2026-05-06 | White House confirms legal breakthrough on the Strategic Bitcoin Reserve covering ~328,372 BTC; no-sale hold… | BTC | +2.80% | May 4-9 2026 (mild, within noise) | high | [[whale-onchain-flows]] |
| 2026-04-22 | Spot ETH ETFs post a 10-day inflow streak (longest since the Jul-2024 launch) - a modest mechanical floor. | ETH | +9.41% | Apr 13-22 2026 ($2,192->$2,398, streak… | high | [[spot-etf-flows]] |
| 2026-04-14 | US spot BTC ETFs post an 8-day, $2.1B net-inflow streak (longest since the Oct-2025 9-day run). | BTC | +3.82% | Apr 14-24 2026 ($74,515 to $77,361) | high | [[spot-etf-flows]] |
| 2026-04-10 | Treasury FinCEN + OFAC issue a joint proposed rule implementing the GENIUS Act's AML/sanctions requirements… | BTC | +2.96% | Apr 8-14 2026 (noise; no isolable move) | high | [[regulatory-approvals-policy]] |
| 2026-03-25 | Zcash (ZEC) +180% as the Grayscale Zcash Trust files to convert to a spot ETF and Multicoin discloses a large… | ZEC | +180.68% | Mar 4-Jun 4 2026 ($222 -> $624; peak… | high | [[spot-etf-flows]] |
| 2026-03-20 | Bittensor's Templar subnet completes Covenant-72B - the largest-ever decentralized LLM pre-training run; TAO… | TAO | +66.53% | March 2026 ($183->$305; intra-month… | high | [[ai-agent-tokens]] |
| 2026-02-23 | Smart-money whales accumulate the Feb-2026 $60-70K panic, then SELL 66% into the bounce to $74K. | BTC | +13% bounce off ~$60K low, then capped as whales distributed at ~$74K | Feb 23 - Mar 2026 | medium | [[whale-onchain-flows]] |
| 2026-01-05 | Memecoin sector spikes +$8B to ~$47B in days (early Jan 2026), then fully round-trips within the month. | PEPE | +77.45% (then round-tripped to ~flat on the month) | intra-Jan-2026 max runup | high | [[memecoin-mania]] |
| 2025-11-28 | Texas executes a ~$5M Bitcoin purchase — first US state to buy BTC with state funds. | BTC | +5.98% | Nov 24-Dec 2 2025 (market recovery… | medium | [[regulatory-approvals-policy]] |
| 2025-10-06 | A 9-day US spot BTC ETF inflow streak carries BTC to its $126,210 all-time high (Oct 6 2025). | BTC | +12.41% | Sep 28-Oct 8 2025 ($109.7k to $123.3k;… | high | [[spot-etf-flows]] |
| 2025-09-30 | Q3 2025: Digital Asset Treasury Companies (DATCos) estimated to deploy ~$22.6B into crypto in a single… | BTC | to >$126k peak (~+100% from early-2025 lows; approximate) | Jan-Oct 2025 | medium | [[corporate-treasury]] |
| 2025-09 | Routine $1B+ USDT mints during the bull market | BTC | +0.4% to +2% | 1h | low | [[stablecoin-supply]] |
| 2025-08-11 | Spot ETH ETFs cross $1B daily net inflow for the first time ever (Aug 11, ETHA $639.8M, FETH $277M). | ETH | +36.2% | 2025-08-04 ($3,498) to 2025-08-13… | high | [[spot-etf-flows]] |
| 2025-07-16 | Arbitrum (ARB) recurring monthly linear unlock tranche, mid-July 2025 | ARB | +16.33% | 8d (2025-07-14 to 2025-07-22) | high | [[token-unlocks-narrative]] |
| 2025-07-14 | ETF-era BTC-led leg: BTC sets records ($122,838 on Jul 14 2025; $126,210 ATH Oct 6 2025) while dominance… | BTC | ATH $122,838 (Jul 14 2025); $126,210 (Oct 6 2025) | 2024-2025 cycle | high | [[bitcoin-dominance-rotation]] |
| 2025-07-14 | US House 'Crypto Week'; CLARITY + GENIUS Acts; Trump signs GENIUS Act July 18. | ETH | +25.16% | Jul 14 ($2,974) to Jul 22 ($3,722);… | high | [[regulatory-approvals-policy]] |
| 2025-07-13 | Aptos (APT) recurring monthly cliff/emission tranche, mid-July 2025 | APT | +13.08% | 6d (2025-07-10 to 2025-07-16) | high | [[token-unlocks-narrative]] |
| 2025-07-11 | Record ETH ETF inflow surge — ETHA largest daily inflow (>$300M), ~$700M weekly; July total $5.46B (+564%… | ETH | +49.62% | 2025-07-01 ($2,487) to 2025-07-22… | high | [[spot-etf-flows]] |
| 2025-07-01 | ETH-treasury accumulation wave: SharpLink + new entrants (BitMine, Tom Lee) ramp ETH buying through summer… | ETH | +53.3% | 2025-06-25 to 2025-07-20 | high | [[corporate-treasury]] |
| 2025-07-01 | Heavy sustained spot BTC ETF inflows through early-mid July 2025. | BTC | +12.09% | 2025-07-01 ($107,136) to 2025-07-14… | high | [[spot-etf-flows]] |
| 2025-07-01 | Sustained stablecoin supply growth through 2025 H2 (aggregate cap heading from ~$250B toward $300B); USDC and… | BTC | +9.96% | 2025-07-01 to 2025-08-15 | high | [[stablecoin-supply]] |
| 2025-06-22 | Texas Gov. Greg Abbott signs SB 21 creating the Texas Strategic Bitcoin Reserve. | BTC | +2.24% | Jun 20-26 2025 (no isolable move,… | medium | [[regulatory-approvals-policy]] |
| 2025-06-04 | Ethereum L1 revival - ETH treasury-company buying, ETF inflows, and renewed staking/DeFi narrative pulled… | ETH | +69.3% | 2025-06-04 to 2025-08-25 | high | [[l1-l2-rotation]] |
| 2025-06-04 | Solana mid-2025 rally leg - renewed SOL momentum amid possible SOL ETF anticipation and usage strength;… | SOL | +50.3% | 2025-06-04 to 2025-09-15 | high | [[l1-l2-rotation]] |
| 2025-06-04 | BNB full-cycle round-trip - BNB ran to a ~$1,312 high then unwound back below its starting level | BNB | +113% | intra-window run-up to ~$1,312 | high | [[l1-l2-rotation]] |
| 2025-05-27 | SharpLink Gaming (SBET) announces pivot to an ETH treasury vehicle (Joe Lubin chairman) | SBET | ~+1,800% to +2,600% (peak) | peak run | medium | [[corporate-treasury]] |
| 2025-05-22 | BTC prints a then-record ~$112K as Moody's US credit downgrade (Aaa->Aa1) drives a safe-haven bid, with… | BTC | to ~$111,970 ATH (then-record) | May 16-22 2025 (Moody's downgrade week) | medium | [[macro-events]] |
| 2025-05-21 | Tether minted $2B USDT (held as inventory) on Tron; BTC made a new ATH around $111,970 the next day (May 22,… | BTC | +1% to +3% | 24h | medium | [[stablecoin-supply]] |
| 2025-04-24 | Initia INIT mainnet launch + airdrop | INIT | +50% | launch | low | [[platform-launches]] |
| 2025-03-21 | US Treasury OFAC lifts sanctions on Tornado Cash after Nov 2024 Fifth Circuit ruling that immutable smart… | TORN | +60% | post-announcement intraday | medium | [[regulatory-bans]] |
| 2025-03-02 | Trump Truth Social post naming BTC, ETH, XRP, SOL, ADA for a US 'Crypto Strategic Reserve'. | ADA | +60% to +69% | weekend Mar 2-3 (intraday peak) | high | [[regulatory-approvals-policy]] |
| 2025-02-21 | SEC agrees in principle to dismiss its enforcement lawsuit against Coinbase under the new (Trump-era,… | COIN | +5% | post-news estimate | medium | [[regulatory-bans]] |
| 2025-01-20 | Trump inauguration / peak risk-on sentiment lifted AI-agent tokens to sector-wide highs | AI-agent sector | ~$17B-$20B aggregate mcap peak | early-mid Jan 2025 | medium | [[ai-agent-tokens]] |
| 2025-01-02 | Fartcoin (largest pump.fun-launched token) hits a new all-time high during peak launchpad froth | FARTCOIN | +44% | 24h | low | [[memecoin-mania]] |
| 2024-12-29 | VIRTUAL (Virtuals Protocol, the AI-agent launchpad on Base) rallied as its agent ecosystem (AIXBT, LUNA,… | VIRTUAL | ATH ~$3.71-$4.50; peak mcap >$1.6B | late Dec 2024 | medium | [[ai-agent-tokens]] |
| 2024-12-15 | FASB ASU 2023-08 fair-value crypto accounting takes effect. | BTC | structural-bullish (no clean single-day move) | diffuse over Q4 2024 | low | [[regulatory-approvals-policy]] |
| 2024-12-09 | Movement MOVE mainnet + token launch | MOVE | +66% | ~24h (to ATH) | medium | [[platform-launches]] |
| 2024-11-29 | Hyperliquid HYPE airdrop — COUNTER-EXAMPLE (squeeze not dump) | HYPE | +~63% | ~first hours (early intraday) | high | [[defi-narratives]] |
| 2024-11-29 | Hyperliquid HYPE genesis airdrop (31% of supply to ~94k points holders); ZERO VC/private allocation | HYPE | +112% | 48h | high | [[platform-launches]] |
| 2024-11-21 | Gary Gensler announces SEC resignation (effective Jan 20, 2025). | XRP | +25% | 24h around Nov 21-22 (3-year high… | high | [[regulatory-approvals-policy]] |
| 2024-11-11 | MicroStrategy buys ~27,200 BTC for ~$2.03B (Oct 31-Nov 10) at ~$74,463 avg; part of post-election… | BTC | +35% to $100k area | Nov-Dec 2024 | high | [[corporate-treasury]] |
| 2024-11-07 | Record single-day spot BTC ETF net inflow of $1.38B (IBIT $1.11B) amid the Trump election win; multi-week… | BTC | +28% | 2024-11-05 (~$69,360) to 2024-11-13… | high | [[spot-etf-flows]] |
| 2024-11-05 | Trump wins US presidential election on an explicitly pro-crypto platform. | BTC | +28% | Election Day Nov 5 (~$69,539 close) to… | high | [[regulatory-approvals-policy]] |
| 2024-11-05 | Trump election victory; stablecoin supply expanded sharply as capital poured into crypto, with aggregate… | BTC | +50% | Nov 5 - Dec 17 2024 | medium | [[stablecoin-supply]] |
| 2024-11 | AIXBT and other flagship agents launched/graduated on the Virtuals bonding curve, driving demand for VIRTUAL… | AIXBT | ATH ~$0.5 (approx) | to late Dec 2024 | medium | [[ai-agent-tokens]] |
| 2024-10-25 | ai16z token launched as an AI-run investment DAO ('Marc AIndreessen'); boosted mid-Nov by a16z-related… | AI16Z | ATH ~$2.47-$2.48 | Jan 1-2, 2025 | high | [[ai-agent-tokens]] |
| 2024-10-10 | Goatseus Maximus (GOAT) launched on pump.fun, tied to the AI 'Truth Terminal' bot; went viral as an early… | GOAT | +several thousand % | ~7d | medium | [[ai-agent-tokens]] |
| 2024-10-01 | Sui (SUI) Move-language L1 breakout - SUI overtook Aptos in market cap (Sep 2024), DEX volume tripled,… | SUI | +110% to +130% | Q4 2024 (Oct-Dec, base ~$1.78-1.97 to… | medium | [[l1-l2-rotation]] |
| 2024-09-18 | Fed delivers a larger-than-expected 50bp rate cut (start of easing cycle) | BTC | +5% | 24h (next day) | high | [[macro-events]] |
| 2024-09 | SSR returned to a low band (~13 cited) that previously coincided with mid-2021, late-2022 and 2024 rebound… | BTC | ~+50% (estimate) | Sep-Dec 2024 | low | [[stablecoin-supply]] |
| 2024-07-01 | ASI token merger went live (AGIX->ASI at ~0.4333, OCEAN->ASI at ~0.4332, 1 FET = 1 ASI); migration of… | ASI | supply consolidation; precise post-merger % uncorroborated | post-merger | low | [[ai-agent-tokens]] |
| 2024-07-01 | Marathon Digital (MARA) adopts full 'HODL' policy — retains all mined BTC and buys on open market (e.g.… | BTC | supportive (supply removed) | ongoing | low | [[corporate-treasury]] |
| 2024-05-28 | Semler Scientific (med-tech) announces BTC as primary treasury reserve, buys 581 BTC for ~$40M | SMLR | ~+30% (close); up to ~+37% intraday | 1d | high | [[corporate-treasury]] |
| 2024-05-23 | SEC approves spot Ethereum ETF 19b-4 filings (May 23); spot ETH ETFs begin trading July 23, 2024. | ETH | +25% to +30% | May 17 (~$3,000) to May 23… | high | [[regulatory-approvals-policy]] |
| 2024-05-22 | US House passes FIT21 market-structure bill. | ETH | +20% to +30% week-of (driven mainly by ETH-ETF approval anticipation, not FIT21) | May 20-23 | low | [[regulatory-approvals-policy]] |
| 2024-04-20 | Fourth Bitcoin halving at block 840,000; block reward cut 6.25 -> 3.125 BTC | BTC | ~+95% | halving to cycle top (~18mo, to… | high | [[bitcoin-halving-narrative]] |
| 2024-04-08 | Metaplanet (Japan) announces it is adopting BTC as a treasury reserve asset; begins accumulation | Metaplanet (3350.T) | ~+4000% to ~+8850% (peak, ~1yr; endpoint-dependent) | 1y cumulative | medium | [[corporate-treasury]] |
| 2024-03-31 | Solana memecoin season peaks (WIF ATH ~Mar 31, BOME/SLERF launches) ahead of a Q2 2024 alt drawdown | WIF | +2000%+ | 2024 to ATH | low | [[memecoin-mania]] |
| 2024-03-28 | Announcement of the Fetch.ai / SingularityNET / Ocean Protocol merger into the Artificial Superintelligence… | FET | ATH ~$3.47 | around Mar 28, 2024 announcement | high | [[ai-agent-tokens]] |
| 2024-03-20 | BlackRock BUIDL tokenized treasury fund launch — institutional validation of RWA narrative | ONDO | +~1,200% | launch-to-peak (2024-01 to 2024-12-16) | medium | [[defi-narratives]] |
| 2024-03-14 | BOME (Book of Meme) launches on Solana during peak memecoin season; Binance listing within days | BOME | +10000%+ | ~2-3d from launch | medium | [[memecoin-mania]] |
| 2024-02-27 | BTC formed a daily golden cross (50-DMA above 200-DMA) in late February 2024 as the spot-ETF-driven rally… | BTC | +15% to +30% | ~30-45d post-cross (to mid-March ATH) | medium | [[technical-signals]] |
| 2024-01 | Solana memecoin season - Pump.fun launch and Solana becoming the global memecoin trading hub; DEX volume… | SOL | +200% | 2024-01 to 2025-01-19 ATH | high | [[l1-l2-rotation]] |
| 2023-12-07 | Jito JTO airdrop (90M tokens, ~$165-225M) to Solana stakers/MEV users | JTO | +150% | 24h | medium | [[platform-launches]] |
| 2023-11-20 | Pyth Network PYTH retrospective airdrop to ~90k wallets (~$77-140M); debut ~$468M mcap | PYTH | +53% | ~4d | low | [[platform-launches]] |
| 2023-10-01 | Solana post-FTX revival - SOL recovered as FTX-estate overhang got priced in/auctioned, Visa USDC settlement… | SOL | +324% | full-year 2023 (~$24 to ~$101.5) | high | [[l1-l2-rotation]] |
| 2023-09 | BTC death cross printed in September 2023 near a local low of the 2023 chop. | BTC | +10% to +20% | ~60d post-cross | medium | [[technical-signals]] |
| 2023-06-14 | EigenLayer opens restaking deposits / points farming begins — restaking narrative ignites | ETH | narrative-driver, not single-token | 12 months | medium | [[defi-narratives]] |
| 2023-04-14 | ARB first post-launch follow-on rally (reported daily jump) | ARB | ~+25% (unverified) | 24h (2023-04-14) | low | [[l1-l2-rotation]] |
| 2023-04 | Accumulation ahead of the April 2024 halving, supercharged by spot ETF anticipation/launch | BTC | ~+150% to +160% | ~12mo into halving (to ~$73.75k ATH) | medium | [[bitcoin-halving-narrative]] |
| 2023-03-10 | Silicon Valley Bank failure + USDC depeg (Circle disclosed $3.3B reserves stuck at SVB); FDIC backstop… | BTC | +18% | ~24h (around Mar 13 backstop) | high | [[macro-events]] |
| 2022-11-10 | US October CPI came in cooler than expected (7.7% YoY vs 8.0% est; 0.4% MoM vs 0.6% est) — sparked hope of… | BTC | +10% | intraday (hours after print) | medium | [[macro-events]] |
| 2022-11 | Post-FTX collapse bottom; SSR fell into a historically low band as stablecoin supply held while BTC market… | BTC | ~+50% to +60% (estimate) | Nov 2022 low to mid-2023 | low | [[stablecoin-supply]] |
| 2022-11 | MVRV ratio fell below 1.0 (price below average cost basis / realized price) during the 2022 bear; ~178 days… | BTC | +150%+ | 12 months from sub-1.0 window | medium | [[technical-signals]] |
| 2022-11 | Funding turned deeply negative during the FTX-collapse cascade. | BTC | +500%+ | Nov 2022 to early 2025 | low | [[technical-signals]] |
| 2021-10-28 | Retail mania / 'Dogecoin-killer' narrative + Robinhood listing speculation drives SHIB to its all-time high | SHIB | +700% to +800% | 30d | medium | [[memecoin-mania]] |
| 2021-08-18 | Avalanche Rush announced - $180M liquidity-mining incentive program bringing Aave and Curve to Avalanche,… | AVAX | +460% | 2021-08-18 to 2021-11-21 | medium | [[l1-l2-rotation]] |
| 2021-05-19 | 2021 alt-season bottom in dominance precedes the May-19 leverage crash. | BTC.D | bottomed ~40%, then rebounded | May 2021 | medium | [[bitcoin-dominance-rotation]] |
| 2021-05-19 | Funding flipped to deep-negative values unseen for months during the May 19 crash. | BTC | +30%+ | weeks post-crash rebound | low | [[technical-signals]] |
| 2021-05-17 | Convex Finance launches; battle to control CRV emissions (Curve wars) escalates | CVX | +~950% to +~2,300% (base-price dependent) | launch to peak (2021-05 to 2022-01) | medium | [[defi-narratives]] |
| 2021-04-28 | Tweets from Elon Musk and Mark Cuban endorsing DOGE | DOGE | +30% | 24h | low | [[memecoin-mania]] |
| 2021-04-16 | Elon Musk tweet ('Doge Barking at the Moon') plus broad retail mania; DOGE hits record high | DOGE | +200% | 24h | medium | [[memecoin-mania]] |
| 2021-02-08 | Tesla discloses $1.5B BTC purchase (bought in January at ~$34,700 avg) and plans to accept BTC as payment | BTC | ~+14.5% | 24h | high | [[corporate-treasury]] |
| 2021-01-28 | Elon Musk tweets 'Doge' and 'Dogecoin is the people's crypto' amid the WallStreetBets/SatoshiStreetBets… | DOGE | +140% | intraday Jan 28 | medium | [[memecoin-mania]] |
| 2021-01 | BSC (Binance Smart Chain, launched Sep 2020) DeFi/yield-farm boom plus Binance accelerator funds; PancakeSwap… | BNB | +1460% | 2021-01 to 2021-05-10 | high | [[l1-l2-rotation]] |
| 2020-08-28 | SushiSwap vampire attack on Uniswap — SUSHI emissions bribe LPs to migrate liquidity | SUSHI | +~200% | launch week | low | [[defi-narratives]] |
| 2020-08 | USDT supply grew strongly (Aug 2020 through Jan 2021) as DeFi summer and the bull market drew USD inflows;… | BTC | +311% | Aug 2020 - Jan 2021 | medium | [[stablecoin-supply]] |
| 2020-07-17 | yearn.finance YFI fair launch (no premine, pure liquidity-mining distribution) | YFI | +~143,000% | ~2 months (launch to ATH) | high | [[defi-narratives]] |
| 2020-06-16 | Compound launches COMP liquidity-mining distribution, kicking off DeFi Summer | COMP | +~400% (intraday, ~$64 to ~$372) | 24h | medium | [[defi-narratives]] |
| 2020-05-11 | Third Bitcoin halving at block 630,000; block reward cut 12.5 -> 6.25 BTC | BTC | ~+700% | halving to cycle top (~18mo) | high | [[bitcoin-halving-narrative]] |
| 2020-04 | BTC daily golden cross (50-DMA above 200-DMA) coming out of the March 2020 COVID crash. | BTC | +30% to +50% | ~90d post-cross | low | [[technical-signals]] |
| 2020-03 | MVRV ratio dipped below 1.0 for ~15 days during the COVID crash. | BTC | +300%+ | 12 months from Mar 2020 low | medium | [[technical-signals]] |
| 2019-07 | Accumulation ahead of the May 2020 halving (buy-the-rumor) | BTC | ~+115% | ~10mo into halving | low | [[bitcoin-halving-narrative]] |
| 2016-07-09 | Second Bitcoin halving at block 420,000; block reward cut 25 -> 12.5 BTC | BTC | ~+290% | 12mo (to 2017-07-09) | high | [[bitcoin-halving-narrative]] |
| 2013-03-16 | Cyprus banking crisis / bail-in of depositors (haircut on bank deposits) | BTC | +~120% | ~Mar 7 (~$42) to Mar 31 (~$92) | low | [[macro-events]] |
| 2012-11-28 | First Bitcoin halving at block 210,000; block reward cut 50 -> 25 BTC | BTC | ~+9000% | halving to cycle top (~12mo) | high | [[bitcoin-halving-narrative]] |

### 🔴 Bearish events (price moved DOWN) — 157

| Date | Narrative / event | Asset | Impact | Window | Conf | Category |
|---|---|---|---|---|---|---|
| 2026-06-03 | SOL high-beta drawdown in the June-2026 'Bitcoin Season' risk-off — NOT the widely-claimed rally. | SOL | -15.93% | Jun 1-4 2026 ($82->$69; low $68.73) | high | [[l1-l2-rotation]] |
| 2026-06-01 | Strategy (MSTR) discloses its first BTC SALE since 2022 - 32 BTC (~$2.5M) for a preferred-dividend payment. | BTC | -4.5% | Jun 1-2 2026 (8-K disclosure, to… | high | [[corporate-treasury]] |
| 2026-05-30 | US Treasury (Bessent) announces seizure of ~$1B in Iranian crypto under 'Operation Economic Fury'. | BTC | -10.81% | May 28-Jun 2 2026 (broad crash, NOT… | high | [[whale-onchain-flows]] |
| 2026-05-28 | Hyperliquid's SPACEX-USDH pre-IPO perp flash-crashes -45% on a faulty oracle mishandling SpaceX's 5-for-1… | SPACEX-USDH (pre-IPO perp) | -45% | 30 min on 2026-05-28 ($2,277 -> $1,254,… | high | [[platform-launches]] |
| 2026-05-21 | Reps. Nick Begich (R-AK) & Jared Golden (D-ME) introduce the American Reserve Modernization Act (ARMA). | BTC | -1.71% | May 19-26 2026 (no positive reaction;… | high | [[regulatory-approvals-policy]] |
| 2026-05-20 | SpaceX S-1 IPO filing discloses 18,712 BTC (fair value $1.293B). | BTC | -2.30% | May 18-22 2026 (broad downtrend; no… | high | [[corporate-treasury]] |
| 2026-05-20 | Butter Bridge (MAP Protocol) hash-collision exploit mints 1 quadrillion MAPO. | MAPO | -96% | intraday 2026-05-20 (~$0.003 ->… | high | [[hacks-exploits]] |
| 2026-05-19 | CFTC sues the State of Minnesota to block its prediction-market felony ban (federal preemption). | BTC | -2.11% | May 17-23 2026 (unrelated market drift;… | low | [[regulatory-approvals-policy]] |
| 2026-05-14 | Senate Banking Committee advances the Digital Asset Market Clarity (CLARITY/DAMA) Act in a 15-9 bipartisan… | BTC | -5.79% | May 12-18 2026 (fell despite the… | high | [[regulatory-approvals-policy]] |
| 2026-05 | Exchange whale ratio spike (top-10 deposits a large share of inflow) | BTC | -3% to -6% | 7d | low | [[whale-onchain-flows]] |
| 2026-04-18 | KelpDAO LRT-collateral exploit cascades into a $15B+ Aave TVL flush (DeFi-wide ~$13B in 2 days). | AAVE | -17.86% | Apr 17-22 2026 | high | [[defi-narratives]] |
| 2026-04-18 | KelpDAO rsETH bridge exploit (~$292M) - 116,500 unbacked rsETH minted, dumped as Aave collateral. | AAVE | -17.86% | Apr 17-22 2026 ($115->$94.5; -26.69%… | high | [[hacks-exploits]] |
| 2026-04-13 | Hyperbridge forged-MMR-proof exploit mints 1 billion bridged DOT on Ethereum, dumped into Uniswap V4. | DOT | -4.8% | intraday 2026-04-13 ($1.22 -> $1.18;… | high | [[hacks-exploits]] |
| 2026-04-01 | Drift Protocol (Solana) drained ~$285M via durable-nonce admin-takeover; DPRK-linked. | DRIFT | -29.52% | Mar 30-Apr 5 2026 (-54.31% intraday) | high | [[hacks-exploits]] |
| 2026-03-22 | Resolv (USR) depegs ~80% after an AWS-KMS private-key compromise mints $80M unbacked USR. | USR | -79.84% | Mar 20-26 2026 ($0.999->$0.20; low… | high | [[stablecoin-depegs]] |
| 2026-03-18 | Largest single-day USDT exchange inflow since Nov 2025 (CryptoQuant), framed as buy-side dry powder | BTC | -6.18% | Mar 16-22 (net); -10.31% intra-window… | medium | [[whale-onchain-flows]] |
| 2026-03-05 | FBI arrests John Daghita for stealing >$46M crypto from US Marshals Service seizure-custody wallets. | BTC | -3.73% | Mar 3-8 2026 (market-driven; not… | high | [[hacks-exploits]] |
| 2026-02-04 | Crypto sells off ~7-9% on USDT-depeg FEARS (no actual depeg) + Tether's retreat from a $20B raise. | BTC | -9.34% | Feb 1-6 2026 ($78,641->$71,297; low… | high | [[macro-events]] |
| 2026-01-30 | Trump nominates Kevin Warsh (a known inflation hawk) as Fed Chair; rate fears sink risk assets. | BTC | -6% | 2026-01-30 day-of nomination | high | [[macro-events]] |
| 2026-01-15 | Large ETH holders move hundreds of millions to exchanges; ETH slips, triggering liquidation cascades. | ETH | sharp multi-week slides + liquidation cascades (part of ETH's -40% YTD / -62% peak-to-trough) | Jan-Feb 2026 | medium | [[whale-onchain-flows]] |
| 2025-12-31 | SharpLink (SBET) ETH-treasury vehicle down ~86-92% from peak; ETH-treasury cohort de-rates as premiums vanish | SBET | ~-86% to -92% from peak | peak to Dec 2025 | low | [[corporate-treasury]] |
| 2025-12-02 | Strategy CEO Phong Le comments on conditions under which the firm would sell BTC; reports note MSTR market… | BTC | toward ~$82k-$86k low (approx) | early Dec 2025 | medium | [[corporate-treasury]] |
| 2025-11-18 | Record IBIT single-day outflow of $523.2M (Nov 18); IBIT November outflows ~$2.34-2.7B (worst month ever)… | BTC | -19.62% | 2025-11-10 ($104,710) to 2025-11-21… | high | [[spot-etf-flows]] |
| 2025-11-16 | BTC 50-DMA crossed below 200-DMA (death cross) ~6 weeks after the Oct 6 ATH near $126k; price had already… | BTC | -14.46% | 2025-11-14 to 2025-11-22 (8d) | high | [[technical-signals]] |
| 2025-11-12 | Strategy (MSTR) mNAV (market cap to BTC NAV) falls below 1.0 for the first time as BTC slides from ~$107k… | BTC | -14.77% | 2025-11-10 to 2025-12-05 | high | [[corporate-treasury]] |
| 2025-11-04 | Stream Finance disclosed a ~$93M loss (external fund manager misappropriation / liquidations stemming from… | xUSD | -74% | to ~$0.26 by early-mid Nov | medium | [[stablecoin-depegs]] |
| 2025-11-03 | Balancer multi-chain exploit of V2 composable stable pools via a rounding-error flaw; ~$128M affected (later… | BAL | ~-4% to -5% | 24h | medium | [[hacks-exploits]] |
| 2025-11-01 | Sustained macro risk-off / liquidity drain through November 2025 (post-October-crash deleveraging, weakening… | BTC | -23.19% | 20d (Nov 1 to Nov 21) | high | [[macro-events]] |
| 2025-11-01 | Post-froth deflation: DOGE (sector bellwether) continues bleeding as risk-off persists and capital… | DOGE | -31.0% | 2025-11-01 to 2025-12-15 (45d) | high | [[memecoin-mania]] |
| 2025-10-28 | US spot Solana ETFs launch (3rd crypto after BTC/ETH) - SOL then crashes ~57% over 4 months. | SOL | -3.47% | Oct 26-31 2025 (launch sell-the-news) | high | [[spot-etf-flows]] |
| 2025-10-10 | BTC tops ~$126k (early Oct) then rolls over; premium-funded buying stalls as mNAVs compress across the cohort | BTC | -9.5% | 2025-10-05 to 2025-10-15 | high | [[corporate-treasury]] |
| 2025-10-10 | Trump announces 100% tariffs on Chinese imports via social media — macro headline into a heavily leveraged… | BTC | -6.38% | Oct 9-12 close-to-close | high | [[macro-events]] |
| 2025-10-10 | Market-wide forced-liquidation cascade (one of the largest in crypto history); on Binance, USDe collateral… | USDe (Binance venue) | -35% | flash low ~$0.65 on Binance | high | [[stablecoin-depegs]] |
| 2025-10-10 | Trump 100% China tariff post triggered a ~$19B liquidation cascade; synthetic stablecoin USDe (Ethena)… | BTC | -8.68% | 2025-10-10 to 2025-10-11 (hourly close) | high | [[stablecoin-supply]] |
| 2025-10-10 | Largest single-day crypto liquidation in history (~$19B+ across exchanges) — a leverage washout amplified by… | BTC | -8.68% | 2025-10-10 to 2025-10-11 (24h) | high | [[technical-signals]] |
| 2025-10-01 | Solana Q4 2025 rotation unwind - SOL de-rated hard as the 2024-25 challenger narrative saturated and the… | SOL | -40.3% | 2025-10-01 to 2025-12-31 | high | [[l1-l2-rotation]] |
| 2025-10 | Top of the 2024-halving cycle (~$126,223 on 2025-10-06) gives way to a sharp drawdown | BTC | -49.6% | max drawdown within 2025-06-04 to… | medium | [[bitcoin-halving-narrative]] |
| 2025-09-25 | Plasma XPL stablecoin-L1 launch + $25M airdrop to ICO pre-depositors; hyper-hyped '$0.1 deposit = $13k' meta | XPL | -58.1% | 30d | high | [[platform-launches]] |
| 2025-09-21 | Story Protocol IP post-spike unwind; large backer/contributor allocation vesting creates persistent overhang | IP | -80.3% | ~60d | high | [[platform-launches]] |
| 2025-08-16 | Arbitrum (ARB) recurring large monthly cliff (team/investor/DAO tranche, ~mid-August 2025) | ARB | -9.52% | 6d (2025-08-14 to 2025-08-20) | high | [[token-unlocks-narrative]] |
| 2025-08-01 | Sui (SUI) monthly cliff unlock (early-investor/team tranche), August 2025 | SUI | -7.56% | 6d (2025-07-29 to 2025-08-04) | high | [[token-unlocks-narrative]] |
| 2025-07-25 | Worldcoin (WLD) large scheduled unlock tranche (investor/team/foundation), late July 2025 | WLD | -9.78% | 6d (2025-07-22 to 2025-07-28) | high | [[token-unlocks-narrative]] |
| 2025-07-12 | Pump.fun PUMP $500M public sale (sold out in ~12 min) + listing; ~$5.5B FDV | PUMP | -25.0% | 30d | high | [[platform-launches]] |
| 2025-07-12 | Pump.fun PUMP ICO raises $600M in 12 minutes (33% of supply, fully unlocked day 1) — then a textbook… | PUMP | -53.57% | Jul 12-Aug 1 2025 ($0.0054->$0.0025;… | high | [[platform-launches]] |
| 2025-07-09 | GMX V1 on Arbitrum exploited for ~$40-42M via cross-contract reentrancy | GMX | ~-28% (from ~$14 to ~$11) | 24h | medium | [[hacks-exploits]] |
| 2025-06-17 | US Senate passes the GENIUS Act (first federal payment-stablecoin framework). | BTC | -2.06% | Jun 17 ($106,842) to Jun 19 ($104,639) | medium | [[regulatory-approvals-policy]] |
| 2025-06-04 | Continued cohort drift lower in mid-2025; AI-agent tokens still bleeding well below their Q1 peaks | AI16Z | -41.71% | 2025-06-04 to 2025-07-01 | high | [[ai-agent-tokens]] |
| 2025-06-04 | TAO traded with the broad AI/alt downtrend in mid-2025, with high intra-window volatility around… | TAO | -13.43% | 2025-06-04 to 2025-06-30 | high | [[ai-agent-tokens]] |
| 2025-06-04 | Post-TGE supply overhang + sector derating measured over trailing 12 months (ENA, PENDLE) | ENA | -66.5% | 12m (intra-window max DD -90.2%) | high | [[defi-narratives]] |
| 2025-06-04 | Trailing-12-month measure of DeFi/yield-token deleveraging and sector derating (CoinGecko) | ONDO | -51.1% | 12m (max DD -80.3%) | high | [[defi-narratives]] |
| 2025-06-04 | Full-year Solana unwind - the complete round-trip of the 2025 challenger rotation into a deep drawdown | SOL | -53.9% | 2025-06-04 to 2026-06-03 | high | [[l1-l2-rotation]] |
| 2025-05-28 | GameStop announces it bought 4,710 BTC (~$500M), first major crypto push; funded via $1.5B April convertible… | GME | -3% to -11% | 1d | medium | [[corporate-treasury]] |
| 2025-05-22 | Cetus Protocol (concentrated-liquidity DEX on Sui) exploited via spoofed tokens + pricing-logic flaw; ~$223M… | CETUS | ~-42% (from ~$0.26 to ~$0.15) | 24h | medium | [[hacks-exploits]] |
| 2025-05-20 | Pyth Network (PYTH) first major unlock: 2.13B PYTH (~$290M, ~21.3% of total supply / ~58.8% of market cap) | PYTH | -13% | 7d pre-unlock | medium | [[token-unlocks-narrative]] |
| 2025-04-03 | Trump 'Liberation Day' tariffs — 10% baseline on all imports, higher rates on China/EU; broad risk-off, S&P… | BTC | -12% | ~48h (early-April high to Apr 7 low… | medium | [[macro-events]] |
| 2025-04-02 | Tron founder Justin Sun publicly accused FDUSD custodian First Digital Trust of being insolvent / having… | FDUSD | -13% to -24% | intraday low ~$0.76-0.87 | medium | [[stablecoin-depegs]] |
| 2025-03-18 | AIXBT agent's autonomous dashboard was accessed by a hacker who queued malicious replies and drained ~55.5… | AIXBT | -16% to -22% | 24h | high | [[ai-agent-tokens]] |
| 2025-03-06 | Trump signs EO establishing the US Strategic Bitcoin Reserve. | BTC | -5% to -6% | Mar 6 intraday high (~$91k) to Mar 7… | medium | [[regulatory-approvals-policy]] |
| 2025-02-25 | Worst-ever spot BTC ETF outflow streak at the time — ~$1.14B single-day outflow Feb 25, multi-billion over… | BTC | -13.5% | 2025-02-24 close $96,984 to 2025-03-04… | medium | [[spot-etf-flows]] |
| 2025-02-21 | Smart-money profit leaders dumped AI-agent positions as the narrative cooled; sector-wide drawdown accelerated | AI16Z | -60% | 30d | medium | [[ai-agent-tokens]] |
| 2025-02-21 | Bybit cold-wallet exploit (Safe UI compromise by Lazarus Group) drained ~401,000 ETH, ~$1.4-1.5B — largest… | ETH | ~-4% to -5% (intraday, ~$2,740 toward ~$2,630) | 24h | medium | [[hacks-exploits]] |
| 2025-02-14 | Argentine President Javier Milei promotes the LIBRA memecoin on X | LIBRA | -89% | ~3 hours from peak | high | [[memecoin-mania]] |
| 2025-02-13 | Bittensor Dynamic TAO (dTAO) upgrade went live, giving every subnet its own Alpha token and liquidity pool;… | subnet alpha tokens | launch spike then -30% to -70% dip | days after each launch | medium | [[ai-agent-tokens]] |
| 2025-02-06 | Berachain BERA mainnet + airdrop (~15.8% supply); large pre-launch vault deposits (Proof-of-Liquidity farming) | BERA | -49% | post-debut spike to settle | high | [[platform-launches]] |
| 2025-02 | Broad AI-agent narrative deflation; top platforms shed market cap and new agent launches collapsed | AI16Z | -75% to -90% | since Jan 2025 | medium | [[ai-agent-tokens]] |
| 2025-01-27 | DeepSeek R1 shock: cheap Chinese open-source AI model triggered a global AI/tech selloff (Nvidia ~-17%) that… | AI-agent sector | sharp decline; sector top confirmed | 24h | high | [[ai-agent-tokens]] |
| 2025-01-19 | Melania Trump launches the MELANIA memecoin one day after TRUMP | MELANIA | -90% | peak to Feb 11 | high | [[memecoin-mania]] |
| 2025-01-19 | TRUMP/MELANIA launch + record pump.fun revenue mark peak memecoin novelty; LIBRA Feb 14 confirms exhaustion | memecoin-sector-mcap | -75% | peak-to-trough | medium | [[memecoin-mania]] |
| 2025-01-17 | Donald Trump launches the OFFICIAL TRUMP memecoin days before his inauguration | TRUMP | -79% | peak (Jan 19) to Feb 11 | high | [[memecoin-mania]] |
| 2025-01-09 | Court greenlight for DOJ to liquidate ~69,370 Silk Road BTC | BTC | -3% | 24h (to ~$93,500) | high | [[whale-onchain-flows]] |
| 2024-10-22 | Scroll SCR TGE; only 7% to airdrop + 5.5% Binance Launchpool, no claim cap so whales scooped supply | SCR | -32% | first day | medium | [[platform-launches]] |
| 2024-10-01 | EigenLayer EIGEN token transferability/debut at ~$6.51B FDV; contentious 5%-to-stakers airdrop, majority to… | EIGEN | -12% | debut day | high | [[platform-launches]] |
| 2024-10-01 | EigenLayer EIGEN airdrop - widely seen as the 'demise of points' | EIGEN | -12% | debut day | high | [[platform-launches]] |
| 2024-08-05 | Yen carry-trade unwind — BoJ hike + weak US jobs data caused the JPY to surge, margin-calling global… | BTC | -15% | 24h | high | [[macro-events]] |
| 2024-08-05 | Yen carry unwind margin calls cascaded into crypto perps | BTC | -15% | 24h | medium | [[macro-events]] |
| 2024-08-05 | Yen carry-trade unwind (BOJ rate hike) margin-called risk assets globally; crypto leverage washed out with… | BTC | -20% to -25% | ~24h peak-to-trough | high | [[technical-signals]] |
| 2024-07-23 | First US spot Ethereum ETFs (ETHA, FETH, ETHE conversion, etc.) begin trading; >$1B day-one volume. | ETH | -3.86% | 2024-07-22 close $3,449 to 2024-07-23… | high | [[spot-etf-flows]] |
| 2024-07-23 | ETHE (Grayscale Ethereum Trust, 2.5% fee) converts to spot ETF; heavy outflows dominate early net ETH ETF… | ETH | -35.4% | 2024-07-22 close $3,449 to 2024-08-05… | medium | [[spot-etf-flows]] |
| 2024-07-05 | Mt Gox rehabilitation trustee announced repayments would begin in early July and started distributing on July… | BTC | -6% | 24h around the early-July move | medium | [[exchange-collapses]] |
| 2024-07-05 | Mt Gox trustee starts BTC creditor repayments; tens of thousands of BTC moved to exchanges | BTC | -7.8% | 24h (~$62,800 to ~$57,900) | high | [[whale-onchain-flows]] |
| 2024-06-30 | EU MiCA stablecoin rules apply; non-compliant stablecoin (USDT) delistings follow. | USDT | EU venue volume sharply down | Q4 2024 to Q2 2025 (USDT trading on EU… | low | [[regulatory-approvals-policy]] |
| 2024-06-26 | Blast BLAST token TGE (~17% of supply, ~$415-430M airdropped); debut ~$3B value | BLAST | -7.7% | launch day | medium | [[platform-launches]] |
| 2024-06-26 | Blast points/gold program drove large pre-TGE TVL; activity fell sharply post-airdrop | BLAST | -7.7% | launch day | medium | [[platform-launches]] |
| 2024-06-20 | LayerZero ZRO 'proof-of-donation' claim (donation required to claim) designed to suppress farmer sell pressure | ZRO | -17% | launch | medium | [[platform-launches]] |
| 2024-06-19 | German BKA dumping ~50,000 seized BTC to exchanges over three weeks | BTC | -17% | campaign peak-to-trough (Jun 19… | high | [[whale-onchain-flows]] |
| 2024-06-17 | ZKsync ZK airdrop (~17.5% supply, 'mother of all airdrops'); heavy farmer selling, weak anti-sybil design | ZK | -27% | first day | high | [[platform-launches]] |
| 2024-05-28 | Large trustee wallet reshuffle ahead of repayment window | BTC | -3% to -5% | 24-48h | low | [[whale-onchain-flows]] |
| 2024-04-05 | FTX estate sold ~25-30M locked SOL at $64/token (~62% discount) to institutions including Galaxy Digital and… | SOL | -6% to -6.5% | 24h around sale | medium | [[token-unlocks-narrative]] |
| 2024-04-03 | Wormhole W token debut + 617M-token airdrop (~$3B FDV); recipients cashed out | W | -24% | first hours | high | [[platform-launches]] |
| 2024-04-02 | Ethena ENA airdrop/claim opens; ATH 2024-04-11 then chronic bleed | ENA | -~87% | ATH (2024-04-11) to 2024 low… | medium | [[defi-narratives]] |
| 2024-02-20 | Starknet STRK airdrop claims went live (~7% of supply); farmers and core dev Nethermind dumped | STRK | -50% | 48h (open-to-trough) | high | [[platform-launches]] |
| 2024-02-20 | Starknet deposits spiked to all-time high ahead of STRK airdrop, then drained | STRK | -50% | 48h post-claim | medium | [[platform-launches]] |
| 2024-01-31 | Jupiter JUP first airdrop ('Jupuary', ~1B tokens); IDO ~$0.40-$0.55 | JUP | -68% | 24h (ATH to next day) | medium | [[platform-launches]] |
| 2024-01-16 | GBTC converts to spot ETF; ~$5.9B left GBTC in January alone, heavy daily forced selling. | BTC | -20% | 2024-01-11 ~$49,000 to 2024-01-23… | high | [[spot-etf-flows]] |
| 2024-01-11 | First 10-11 US spot Bitcoin ETFs (IBIT, FBTC, GBTC conversion, ARKB, etc.) begin trading; SEC approved Jan… | BTC | -14.06% | 2024-01-11 close $46,369 to 2024-01-23… | high | [[spot-etf-flows]] |
| 2024-01-10 | SEC approves 11 US spot Bitcoin ETFs; trading begins Jan 11. | BTC | -14% to -19% | Jan 10-11 high (~$46k-$49k) to Jan 23… | high | [[regulatory-approvals-policy]] |
| 2024-01-01 | dYdX (DYDX) six recurring monthly unlocks of ~33M tokens each (H1 2024) following the December 2023 cliff | DYDX | -5% to -10% | per monthly unlock window | low | [[token-unlocks-narrative]] |
| 2023-12-01 | dYdX (DYDX) cliff unlock: 150M DYDX (~$505M, ~30% of allocation / ~80% of then-circulating supply) released… | DYDX | -2% to -5% | 24h | medium | [[token-unlocks-narrative]] |
| 2023-11-21 | Binance settled US DOJ/CFTC/Treasury criminal charges for $4.3B; CEO Changpeng Zhao (CZ) resigned and pleaded… | BNB | -7%+ | intraday Nov 21 (sold off on the… | high | [[exchange-collapses]] |
| 2023-11-12 | Aptos (APT) scheduled monthly cliff unlock (~24.8M APT, ~10.9% of circulating supply; one of the recurring… | APT | ~-10% to -20% (approx) | around unlock | low | [[token-unlocks-narrative]] |
| 2023-10-11 | USDR (Tangible) treasury drained of liquid DAI by redemptions; most backing was illiquid tokenized real… | USDR | -49% | hours, low ~$0.50-0.51 | high | [[stablecoin-depegs]] |
| 2023-07-30 | Curve Vyper reentrancy exploit drains multiple pools; Egorov's ~$60-100M CRV-backed loans threaten bad debt | CRV | -~13% | 24h (larger intraday peak-to-trough… | high | [[defi-narratives]] |
| 2023-07-30 | Curve Finance Vyper compiler reentrancy bug (Vyper 0.2.15/0.2.16/0.3.0) drained ~$52-70M across multiple… | CRV | -15% to -17% | 24h | medium | [[hacks-exploits]] |
| 2023-07-07 | Multichain (cross-chain router) lost control of keys; ~$126M unauthorized transfers from Fantom/Moonriver… | MULTI | ~-16% (to ~$2.60) | 24h | medium | [[hacks-exploits]] |
| 2023-06-15 | Curve 3pool imbalance — a whale borrowed and swapped tens of millions of USDT for USDC, tilting the pool to… | USDT | -0.3% | low ~$0.997 | medium | [[stablecoin-depegs]] |
| 2023-06-05 | SEC sues Binance (June 5) and Coinbase (June 6), naming ~12-13 tokens (SOL, ADA, MATIC, FIL, SAND, AXS, etc.)… | SOL | -17% | few days | medium | [[regulatory-bans]] |
| 2023-03-23 | Arbitrum ARB airdrop / TGE | ARB | settled to ~$1.20-1.25 within days of a much higher launch print | ~4 days | medium | [[defi-narratives]] |
| 2023-03-22 | Coinbase discloses SEC Wells notice (leading indicator of the June 2023 suit) | COIN | -8% | next-day estimate | low | [[regulatory-bans]] |
| 2023-03-13 | Euler Finance flash-loan attack drained ~$197M (stETH, WBTC, DAI, USDC) via a flaw in the donateToReserve /… | EUL | -45% to -50% | 24h | medium | [[hacks-exploits]] |
| 2023-03-11 | Circle disclosed ~$3.3B of USDC reserves stuck at the failed Silicon Valley Bank; depeg worsened over the… | USDC | -12% | low ~$0.877 Mar 11 | high | [[stablecoin-depegs]] |
| 2023-03-11 | Circle disclosed $3.3B of USDC reserves were stuck at the failed Silicon Valley Bank; USDC depegged to… | USDC | -12% to -13% (to ~$0.87-0.88) | Mar 11 | high | [[stablecoin-supply]] |
| 2022-11-28 | BlockFi filed for Chapter 11 bankruptcy, citing exposure to FTX/Alameda (FTX had extended BlockFi a credit… | BTC | -1% to -3% | 24h (BTC ~$16,400, deep in post-FTX… | low | [[exchange-collapses]] |
| 2022-11-16 | Genesis Global Capital halted withdrawals on its lending arm on Nov 16, 2022 due to FTX exposure; Gemini Earn… | BTC | -2% to -4% | 24h (added to ongoing FTX selloff) | low | [[exchange-collapses]] |
| 2022-11-08 | CoinDesk report (Nov 2) exposed Alameda Research's balance sheet was dominated by FTX's own FTT token;… | FTT | -75% to -78% | 24h | high | [[exchange-collapses]] |
| 2022-11-08 | FTX collapse / contagion forced deleveraging; funding turned deeply negative. | BTC | -26% | ~2 weeks (~$21k to ~$15.5k low) | high | [[technical-signals]] |
| 2022-08-01 | Nomad bridge: a faulty upgrade made any message provable, triggering a chaotic 'free-for-all' that drained… | bridged-assets | depeg / sharp drop on affected wrapped assets | 24h | medium | [[hacks-exploits]] |
| 2022-07-20 | Tesla reveals it converted ~75% of its BTC to fiat in Q2 2022 (~$936M, ~30k BTC sold at ~$29k avg), citing… | BTC | ~-2% (approx) | intraday post-report | medium | [[corporate-treasury]] |
| 2022-06-27 | Three Arrows Capital (3AC), a multi-billion-dollar crypto hedge fund, defaulted after its LUNA/stETH/GBTC… | BTC | -33% to -35% | ~2 weeks into the Jun 18 low (~$17,600) | high | [[exchange-collapses]] |
| 2022-06-13 | Post-Terra fear spread to Tron's algorithmic USDD; coordinated selling pushed it off peg | USDD | -9% | intraday low ~$0.91 | medium | [[stablecoin-depegs]] |
| 2022-06-12 | Celsius Network paused all withdrawals, swaps and transfers on June 12, 2022 citing 'extreme market… | BTC | -15% | 24h (from ~$27k to ~$23,300 on Jun 13) | high | [[exchange-collapses]] |
| 2022-05-12 | Terra-contagion panic spilled into USDT; redemption fears and thin venue books briefly pushed USDT off peg on… | USDT | -8% | flash low ~$0.92 on Kraken | medium | [[stablecoin-depegs]] |
| 2022-05-12 | Terra/UST collapse triggered a redemption run on Tether; USDT processed billions in redemptions and supply… | BTC | -13% | May 5-12 2022 (Terra week) | medium | [[stablecoin-supply]] |
| 2022-05-09 | UST broke peg after large Anchor withdrawals and coordinated Curve 4pool/UST selling; reflexive LUNA minting… | UST | -98% | 7d, low ~$0.02 by May 13 | high | [[stablecoin-depegs]] |
| 2022-05-09 | TerraUSD (UST) algorithmic stablecoin lost its $1 peg and entered a death spiral with LUNA; UST went to… | UST | -100% | May 8-13 | high | [[stablecoin-supply]] |
| 2022-05 | Sustained redemptions through the post-Terra bear deepening (3AC, Celsius collapses) | BTC | -50% | May-Jun 2022 | medium | [[stablecoin-supply]] |
| 2022-03-29 | Ronin bridge (Axie Infinity) drained ~$625M (173,600 ETH + 25.5M USDC) via 5 compromised validator keys;… | RON | ~-23% | 24h | high | [[hacks-exploits]] |
| 2022-02-02 | Wormhole bridge exploit: attacker forged a signature to mint 120,000 wETH (~$320-326M) on Solana without… | SOL | ~-13.5% | 24h | high | [[hacks-exploits]] |
| 2022-01-01 | Curve wars peak then multi-year structural decay of emission tokens | CVX | -90%+ | peak to 2023 lows | low | [[defi-narratives]] |
| 2021-11-23 | Indian government lists 'The Cryptocurrency and Regulation of Official Digital Currency Bill, 2021' to ban… | BTC | -15% to -17% | intraday (Indian venues) | medium | [[regulatory-bans]] |
| 2021-11-21 | Post-2021-bull L1 unwind - AVAX and all 2021 'ETH-killers' collapsed as incentive programs tapered and the… | AVAX | -94% | 2021-11-21 ATH to 2022 bear low | high | [[l1-l2-rotation]] |
| 2021-11-10 | Cycle ATH ~$69k with MVRV-Z making a LOWER high than April (bearish divergence) — realized cap had caught up… | BTC | -77% | Nov 2021 to Nov 2022 (cycle) | medium | [[technical-signals]] |
| 2021-11 | Top of the 2020-halving cycle (~$69,000) gives way to the 2022 bear, amplified by Terra/LUNA, Celsius, 3AC,… | BTC | -77% | peak-to-trough (~12mo) | high | [[bitcoin-halving-narrative]] |
| 2021-09-24 | PBOC and ten agencies declare ALL cryptocurrency-related transactions illegal | BTC | -8% | 24h close-to-close | high | [[regulatory-bans]] |
| 2021-08-10 | Poly Network cross-chain exploit drained ~$610-612M across Ethereum, BSC and Polygon via a contract-call flaw | affected-tokens | limited/transient (funds returned within ~2 weeks) | 7d | medium | [[hacks-exploits]] |
| 2021-06-21 | China intensifies mining crackdown; Sichuan and other provinces order miners to shut down, accelerating the… | BTC | -10% | intraday | medium | [[regulatory-bans]] |
| 2021-06-16 | Large TITAN holders sold near the peak (~$60-65), IRON broke peg below $0.75, triggering crypto's first… | IRON | -25% | intraday low below $0.75 | high | [[stablecoin-depegs]] |
| 2021-05-19 | BTC closed below its 200-day SMA (~$39,825) for the first time since 29 Apr 2020, breaking a key watched… | BTC | -30% | intraday 19 May 2021 (open ~$43k to low… | high | [[technical-signals]] |
| 2021-05-19 | Leverage washout as BTC broke the 200-DMA; >$8B liquidations across the market. | BTC | -30% | intraday 24h (to ~$28.8k low; ~33.9%… | high | [[technical-signals]] |
| 2021-05-18 | Three Chinese financial associations reiterate ban on financial firms providing crypto services; State… | BTC | -38% | peak-to-trough (May12-May19 low ~$36k) | high | [[regulatory-bans]] |
| 2021-05-10 | 2021 alt-season: BTC dominance collapses as DOGE/BNB/altcoins blow off. | BTC.D | ~73% to ~40% (-33pp) | Jan-May 2021 | medium | [[bitcoin-dominance-rotation]] |
| 2021-05-10 | Internet Computer (ICP) public launch with aggressive early seed/investor token availability and ~$40B+ FDV;… | ICP | -39% | launch-day intraday | medium | [[token-unlocks-narrative]] |
| 2021-05-08 | Elon Musk hosts Saturday Night Live; called himself 'the Dogefather'. Classic scheduled-event sell-the-news. | DOGE | -30% | during SNL broadcast (~hours) | high | [[memecoin-mania]] |
| 2021-05-08 | Memecoin froth peaks (DOGE SNL ATH May 8, SHIB launch hype) coinciding with the 2021 cycle's first major top;… | memecoin-sector-mcap | -78% to -80% | peak-to-trough | medium | [[memecoin-mania]] |
| 2021-04 | MVRV Z-score spiked to roughly ~7 at the April 2021 local top. | BTC | -50% | Apr to Jul 2021 (peak-to-trough) | medium | [[technical-signals]] |
| 2021-04 | Perpetual funding (e.g. BitMEX XBTUSD) ran elevated, around 0.2-0.3% per 8h at times, into the April 2021… | BTC | -50% | Apr to Jul 2021 | low | [[technical-signals]] |
| 2020-12-22 | SEC sues Ripple Labs and executives, alleging XRP was a $1.3B unregistered securities offering | XRP | -52% | 24h | high | [[regulatory-bans]] |
| 2020-09-25 | KuCoin hot-wallet hack drained ~$275-281M (BTC, ETH, USDT, XRP, LTC, $147M ERC-20s, $87M Stellar tokens) | BTC | modest / short-lived (loss socialized) | 24h | medium | [[hacks-exploits]] |
| 2020-09-17 | Uniswap UNI airdrop (400 UNI to every past user) | UNI | 75% of recipients sold within 7d | 7d | high | [[defi-narratives]] |
| 2020-03-12 | COVID-19 global panic; S&P 500 limit-down; worldwide dash-for-cash forced liquidation of all risk assets | BTC | -40% | 24h (Mar 12) | high | [[macro-events]] |
| 2020-03-12 | COVID dash-for-cash hit a leveraged BitMEX-dominated market; cascade amplified the macro shock | BTC | -50% | intraday wick (~$8k to ~$3.8-4k) | high | [[macro-events]] |
| 2018-01-11 | South Korea justice minister says the government is preparing a bill to ban crypto exchanges | BTC | -12% | intraday | medium | [[regulatory-bans]] |
| 2018-01-07 | ICO-era alt-mania drives BTC dominance to a cycle low (~33%) at the top. | BTC.D | fell to ~33% at the top | Dec 2017-Jan 2018 | medium | [[bitcoin-dominance-rotation]] |
| 2017-12 | Top of the 2016-halving cycle (~$19,700-$19,800) gives way to the 2018 'crypto winter' | BTC | -84% | peak-to-trough (~12mo) | high | [[bitcoin-halving-narrative]] |
| 2017-09-04 | PBOC + CSRC joint statement declares ICOs illegal fundraising; days later China orders domestic exchange… | BTC | -5% to -18% | 24h (estimates conflict) | medium | [[regulatory-bans]] |
| 2014-02-07 | Mt Gox — then the largest Bitcoin exchange — halted all BTC withdrawals on Feb 7, suspended trading Feb 24,… | BTC | -36% | 1 Feb 2014 to end of March 2014 (Mt Gox… | high | [[exchange-collapses]] |
| 2013-12-05 | People's Bank of China bars financial institutions from handling Bitcoin transactions; BTC China then halts… | BTC | -55% | peak-to-trough ~weeks | medium | [[regulatory-bans]] |
| 2013-12 | Top of the 2012-halving cycle (~$1,160) gives way to bear market, amplified by the Feb 2014 Mt. Gox collapse | BTC | -85% | peak-to-trough (~13mo) | high | [[bitcoin-halving-narrative]] |

### ⚪ Flat / no-isolable-move events (the 'fake signals' & structural) — 34

*The most important section for a backtester: narratives that looked tradeable but produced no clean spot move — structural adoption, priced-in policy, depeg-fear-without-depeg, wallet-≠-sell, ETF-≠-floor. Do not trade these as standalone spot triggers.*

| Date | Narrative / event | Asset | Impact | Window | Conf | Category |
|---|---|---|---|---|---|---|
| 2026-06-03 | Bitcoin Season persists: BTC.D ~58-58.7%, Altcoin Season Index ~49, ~249 days since the last alt-season. | BTC.D | ~58.7% (Bitcoin Season; ASI ~49) | early June 2026 | high | [[bitcoin-dominance-rotation]] |
| 2026-05-26 | Total stablecoin market cap hits a record ~$322B (exceeds the FX reserves of 95 nations). | stablecoin-supply | record ~$322B (dry powder); no spot lift — BTC fell ~40% YTD into June 2026 | May 2026 | high | [[stablecoin-supply]] |
| 2026-05-22 | Trump Media transfers 2,650 BTC (~$205M) to Crypto.com (says 'did not sell'). | BTC | +0.44% | May 20-25 2026 (flat; 'bearish… | high | [[corporate-treasury]] |
| 2026-03-08 | Tokenized RWAs (ex-stablecoins) surge to ~$25-32B in 2026; Ethereum + L2s dominate. | ETH | structural fundamental tailwind (no clean spot catalyst; ETH -40% YTD regardless) | 2026 | medium | [[defi-narratives]] |
| 2026-03 | Large apparent ETF outflows partly attributed to institutional repositioning | BTC | flat-to-down | weeks | low | [[whale-onchain-flows]] |
| 2026-02-19 | Aave (Horizon market) becomes the first DeFi lending protocol to cross $1B in tokenized-RWA deposits. | AAVE | fundamental milestone (no clean spot catalyst; coincided with broad outflows) | Feb 2026 | high | [[defi-narratives]] |
| 2026-02-15 | OpenSea confirms SEA token (Q1 2026): 50% community airdrop + 50% of revenue to buy back SEA… | SEA | TBD (design-confirmed; token just launching, not yet measurable) | Q1 2026 | low | [[platform-launches]] |
| 2026-01-20 | A 13-year-dormant Bitcoin whale moves 909 BTC (~$84-85M) from a 2013 wallet to a new address. | BTC | no isolable impact (panic headline; no exchange deposit, no follow-through sell) | mid-Jan 2026 | high | [[whale-onchain-flows]] |
| 2026-01 | SSR fell toward a low band (~21 cited) / liquidity equilibrium, but analysts (Axel Adler Jr.) flagged the… | BTC | flat-to-down | early 2026 | low | [[stablecoin-supply]] |
| 2025-10 | Repayment deadline extended to Oct 2026; periodic large BTC transfers | BTC | modest / sentiment-driven | 24h | medium | [[whale-onchain-flows]] |
| 2025-09-17 | September 2025 FOMC rate cut (anticipated/priced) | BTC | +0.25% | Sep 16-19 close-to-close | high | [[macro-events]] |
| 2025-07-21 | Coinbase launches the first CFTC-regulated crypto perpetual futures for US traders. | BTC | -0.94% | Jul 18-24 2025 (no isolable move) | high | [[regulatory-approvals-policy]] |
| 2025-07-18 | OG whale's ~80,000 BTC routed to Galaxy Digital OTC desk and sold ($9B estate sale) | BTC | +0.31% (Jul 14-27 net); -6.19% intra-window drawdown | Jul 14-27 (~10-day sale program) | high | [[whale-onchain-flows]] |
| 2025-07-04 | Eight Satoshi-era wallets move 80,000 BTC to new (non-exchange) addresses | BTC | +0.04% (Jul 3-8 net); -2.57% intra-window drawdown | Jul 3-8 (surrounding days) | high | [[whale-onchain-flows]] |
| 2025-07-01 | Optimism (OP) recurring monthly unlock tranche, early July 2025 | OP | -0.12% | 6d (2025-06-28 to 2025-07-04) | high | [[token-unlocks-narrative]] |
| 2025-03-01 | FTX-related vested SOL fully unlocked (~11.2M SOL, ~2.2% of supply; the biggest single SOL unlock to date),… | SOL | priced-in / no clean adverse day-of move (slight rebound ~$136 to ~$140) | around 2025-03-01 | medium | [[token-unlocks-narrative]] |
| 2025-01-23 | SEC issues SAB 122, rescinding SAB 121. | BTC | flat-to-modestly-positive | Jan 23-27 (BTC near $103-105k… | medium | [[regulatory-approvals-policy]] |
| 2025 | Year-long wave of dormant-whale reactivations and sales | BTC | net flat-to-up over year despite billions sold | 2025 full year | medium | [[whale-onchain-flows]] |
| 2024-12-02 | US government transfers ~$2B Silk Road BTC to Coinbase Prime | BTC | ~flat (approx +0.4% to -0.03%) | 24h | low | [[whale-onchain-flows]] |
| 2024-05-01 | FTX estate third SOL sale round: ~1.8M SOL for ~$232M, part of ~41M SOL liquidated across three auctions | SOL | unclear / not corroborated (no clean +11% confirmed) | 24h | low | [[token-unlocks-narrative]] |
| 2024-04-30 | Asia's first spot BTC and ETH ETFs (China AMC, Bosera HashKey, Harvest) debut on HKEX with in-kind creation. | BTC | ~0% to slightly down | 2024-04-30 launch week | medium | [[spot-etf-flows]] |
| 2024-03-16 | Arbitrum (ARB) first major cliff: ~1.11B ARB unlocked (team/investors/DAO, ~$1.2B notional), expanding… | ARB | ~flat day 1 | day 1 | medium | [[token-unlocks-narrative]] |
| 2024-03 | MVRV Z-score reached only ~3-4 at the $100k+ ATH — elevated but well below historical >7 extremes. | BTC | +0% (signal-flat, no extreme) | n/a | medium | [[technical-signals]] |
| 2024-03 | BitMEX max funding only ~0.13% in 2024 even as BTC made new highs; sustained high rates effectively… | BTC | +0% (signal-flat) | n/a | low | [[technical-signals]] |
| 2024-02-21 | Nigeria blocks access to crypto exchange websites (Binance, Coinbase, etc.) and detains two Binance… | the named coin | 0% | global price (no measurable effect) | medium | [[regulatory-bans]] |
| 2023-11-01 | FTX/Alameda estate began redeeming staked SOL and routing it through estate-controlled addresses for… | SOL | no material negative impact | ongoing | low | [[token-unlocks-narrative]] |
| 2023-08-09 | Coinbase Base L2 public mainnet launch - 'Onchain Summer' campaign; no native token, speculation routed into… | ETH | ~$68M ETH bridged pre-launch (flow signal, not a price move) | launch weekend | high | [[l1-l2-rotation]] |
| 2023-05-03 | Sui (SUI) mainnet and token launch - heavily marketed Move-language L1 debut | SUI | launch-day price discovery (volatile debut) | launch 2023-05-03 | medium | [[l1-l2-rotation]] |
| 2023-03-23 | Arbitrum ARB airdrop / token generation event - 12.75% of supply airdropped to early users and DAOs | ARB | ~$1.8B market cap in first ~2 hours; launch-day price discovery | launch day 2023-03-23 | high | [[l1-l2-rotation]] |
| 2023-01-19 | Genesis Global Capital filed for Chapter 11 bankruptcy, the final major domino, after halting withdrawals in… | BTC | +2% to flat | 24h (BTC ~$21,000 and rising — market… | low | [[exchange-collapses]] |
| 2022-10-19 | Aptos (APT) mainnet token launch - 'Solana-killer' Move L1 from ex-Meta Diem team, launched into a bear market | APT | launch-day price discovery, volatile debut | launch 2022-10-19 | medium | [[l1-l2-rotation]] |
| 2022-07-05 | Voyager Digital suspended all trading, deposits and withdrawals on July 1, 2022, then filed for Chapter 11… | BTC | flat to -3% | 24h (largely priced in by then, BTC… | low | [[exchange-collapses]] |
| 2022-07-01 | India's 1% TDS on crypto transfers takes effect (announced Feb 1 2022 budget alongside 30% gains tax) | the named coin | 0% | global price (no effect) | high | [[regulatory-bans]] |
| 2020-08-11 | MicroStrategy announces first BTC purchase, 21,454 BTC for $250M at ~$11,653, calling BTC 'superior to cash'… | BTC | ~+1% | 24h | high | [[corporate-treasury]] |

## Related

- [[crypto-narratives-overview]] — the catalog hub, analog-mechanism map, and methodology
- Machine-readable source: `catalog/all-narratives.json`
