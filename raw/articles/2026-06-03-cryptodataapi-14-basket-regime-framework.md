<!-- Source: https://cryptodataapi.com/regimes -->
<!-- Captured: 2026-06-03 -->
<!-- Publisher: Crypto Data API — VENTURE AI LABS -->

# Crypto Data API — Market Regimes (14 meta-baskets)

Live market snapshot at capture (2026-06-03): Total Market Cap $2.40T (-2.52%), 24h Volume $206.19B, BTC Dominance 59.3%, Market Health 30/100 BEARISH, Short-Term 33/100 BEARISH, Long-Term 28/100 BEARISH, Open Interest $54.16B (+0.21%), 24h Liquidations $727.17M, Long/Short 63.9% / 36.1%.

> 14 meta-baskets that capture every state crypto markets can be in — up, down, sideways, euphoric, broken, squeezing. Each basket implies a different set of coins, leverage levels, holding durations, and funding cost tolerance. Designed for systematic perps trading on venues like Hyperliquid.

| # | Meta-Basket | Primary Timescale | Directional Bias | Data |
|---|---|---|---|---|
| 1 | Macro Trend | Months | Long / Short | live |
| 2 | BTC Cycle | Weeks – Months | Long / Neutral | live |
| 3 | Meme / Speculative | Hours – Days | Long / Short | coming soon |
| 4 | Derivatives-Native | Minutes – Days | Both | live |
| 5 | Event / Catalyst | Hours – Weeks | Both | coming soon |
| 6 | Macro Correlation | Days – Weeks | Short / Long | live |
| 7 | On-Chain Intelligence | Days – Weeks | Leading signal | live |
| 8 | Carry Trade / Basis | Days – Weeks | Regime health | live |
| 9 | Liquidity / Market Depth | Real-time – Days | Size / risk filter | regime classifier |
| 10 | Institutional Flow | Weeks – Months | Structural floor | live |
| 11 | Security / Black Swan | Hours – Days | Short then long reversal | coming soon |
| 12 | Geopolitical / Policy Shock | Hours – Weeks | Both | coming soon |
| 13 | Volatility Regime | Days – Weeks | Risk sizing overlay | coming soon |
| 14 | Technical / Structural | Hours – Days | Universal overlay | coming soon |

## 01 — Macro Trend (Months, Long/Short)
Broadest backdrop — sets the regime everything else trades inside of. Duration 1–6 months. Driven by structural market posture (HH/HL vs LH/LL), aggregate funding, and BTC dominance flow.
- **Full Bull Run** (Long): HH/HL structure, rising funding, BTC dominance dropping. Long majors + alts, trail stops, scale out at euphoria.
- **Altcoin Season** (Long alts): BTC.D falling below 55–60%, capital rotating out of BTC. Long ETH/SOL/alts, flat BTC.
- **Full Bear Market** (Short): LH/LL structure, negative funding, rising BTC.D. Short alts, fade dead-cat bounces, smaller size.
- **Accumulation / Range** (Neutral): Compressed vol, low-trend OI, stable funding. Mean reversion, range fade, tight TP/SL.
- **Sideways / Chop** (Both): Low ATR, mixed funding, no structural bias. Reduce size, tighter range, avoid breakout plays.
- **Distribution Phase** (Short setup): Rising OI with price stalling, funding bleeding positive. Prepare shorts, trail longs aggressively.

## 02 — BTC Cycle (Weeks–Months, Long/Neutral)
BTC has distinct cycles that don't always track the broader market — halving supply shocks, miner flows, dominance rotations. Tradeable independently of alts.
- **BTC Solo Bull Run** (Long BTC): BTC.D rising while alts flat/down; BTC leading price discovery. 1–2 week persistent runs historically precede alt rotation.
- **Pre-Halving Ramp** (Long BTC): Historical ~60–90 day pre-halving accumulation pattern.
- **Post-Halving Lag** (Neutral → Long): Miner sell pressure subsides, supply shock builds over ~6–12 months.
- **BTC Risk-Off Sell** (Short BTC): Correlates with Nasdaq/equities selling, macro fear spike.

## 03 — Meme / Speculative (Hours–Days, Long/Short)
Isolated, often Solana-based cycles. Single-coin or basket vol blasts driven by social momentum and lowcap rotation — uncorrelated to majors.
- **Meme Coin Bull Run** (Long basket): Correlated pump across DOGE/PEPE/WIF/BONK; BTC.D falling, retail FOMO active.
- **Single Meme Pump** (Long): Viral social catalyst, volume spike 10x+ on a low-cap coin.
- **Single Meme Tank** (Short): Post-pump fade, rug narrative, founder exit signal.
- **Lowcap Pump/Dump** (Long → Short): Low mcap, OI spike, whale accumulation on-chain; exit after first 2–3x.

## 04 — Derivatives-Native (Minutes–Days, Both)
Perps-native setups that don't exist in spot — funding rates, OI imbalance, liquidation cascades. Highly relevant for Hyperliquid where leverage and on-chain transparency expose positioning fragility.
- **Funding Rate Extreme (Long)** (Fade longs): Funding >0.1% per 8h sustained; longs overheated, reversal imminent.
- **Funding Rate Extreme (Short)** (Fade shorts): Sustained deeply negative funding; shorts overextended, likely squeeze.
- **Liquidation Cascade Down** (Short → Long): Large long liquidation cluster hit, cascade accelerates, then snap reversal.
- **Liquidation Cascade Up** (Long → Short): Short squeeze cascade; OI collapses as shorts are flushed.
- **OI Divergence** (Counter-trend): Price rising but OI falling = weakening trend; price falling but OI rising = conviction shorts.
- **Funding Rate Arbitrage** (Delta-neutral): Positive funding: short perp + long spot. Negative funding: long perp + short spot.
- **Long/Short Squeeze Setup** (Both): Build-up of lopsided OI on one side; triggers forced unwind.

## 05 — Event / Catalyst (Hours–Weeks, Both)
Short-duration, high-conviction windows triggered by discrete events — listings, unlocks, narrative pumps, regulatory news, macro prints, stablecoin depegs.
- **Exchange Listing** (Long pre-listing): Rumor phase pre-pump on listing announcement; fade after 1–3 days post-listing.
- **Narrative / Sector Pump** (Long sector): AI tokens, DePIN, RWA, GameFi trending — capital rotates in fast.
- **Sector Rotation** (Long in / Short out): Money flows DeFi → AI → Gaming. Short peaked sector, long the next.
- **Protocol Event** (Varies): Mainnet launch, token unlock, major upgrade — price often dumps unlocks, pumps launches.
- **Token Unlock / Vesting** (Short bias): Large scheduled unlock approaching = sell pressure on high-FDV tokens.
- **Regulatory News** (Both): SEC news, ETF approval/rejection, country ban — sharp vol spike both ways.
- **Macro Print Event** (Risk on/off): CPI, Fed rate decision, FOMC — BTC and ETH trade like Nasdaq during these windows.
- **Stablecoin Depeg** (Short majors): USDT/USDC/algo stablecoin depeg triggers panic selling, BTC vol spikes.

## 06 — Macro Correlation (Days–Weeks, Short/Long)
Where crypto follows external forces — equities, dollar strength, gold, treasury yields. Crypto increasingly trades as a high-beta tech asset.
- **Risk-Off (Equities Sell)** (Short crypto): Nasdaq/S&P dropping, DXY rising, gold rising — BTC follows equities.
- **Risk-On (Equities Rally)** (Long crypto): Tech stocks ripping, DXY falling, low vol — BTC leads, alts follow.
- **Dollar Strength (DXY Spike)** (Short alts): DXY >105 typically suppresses all risk assets including crypto.
- **Gold/Copper Ratio Shift** (Risk sentiment): Copper/Gold ratio rising = risk-on globally; falling = macro fear.

## 07 — On-Chain Intelligence (Days–Weeks, Leading signal)
Blockchain data as a leading — not lagging — indicator: exchange flows, whale accumulation, miner behavior, supply dormancy.
- **Exchange Inflow Spike** (Short setup): Large coin inflows to exchanges precede sell-offs.
- **Stablecoin Dry Powder** (Long setup): Large stablecoins sitting on exchanges = dry powder for buying.
- **Whale Accumulation** (Long): Silent large wallet buildup detected on-chain = leading long signal.
- **Supply Shock / Dormancy** (Distribution warning): Long-dormant coins moving = distribution warning.
- **Miner Capitulation** (Bottom signal): Miners dumping = typically a late-bear bottoming signal.
- **On-Chain Health Score** (Composite): Composite of flows, dormancy, miner pressure, active addresses.

## 08 — Carry Trade / Basis (Days–Weeks, Regime health)
The futures basis (perp vs spot spread) is its own regime. Basis collapse historically precedes the clearest cascade warnings — persistent positive funding + record OI = fragility.
- **High Basis (8%+ APR)** (Fragile): Carry trade crowded, leverage building, fragility forming.
- **Healthy Basis (3–6%)** (Sustainable): Sustainable accumulation, best long environment.
- **Basis Collapse / Inversion** (Cascade likely): Backwardation, fear extreme, carry traders exiting, cascade likely.
- **Flat / Marginal Basis** (Range-bound): <4% basis, institutional capital sidelined, range-bound fragility.

## 09 — Liquidity / Market Depth (Real-time–Days, Size/risk filter)
Answers how the market is moving. OI growing faster than order-book depth was the single clearest pre-crash warning in the October 2025 cascade. Hyperliquid's on-chain transparency makes this uniquely trackable. Backed by per-minute L2 book snapshots across the top-25 HL perps + per-coin regime classifier.
- **Deep Book, Tight Spreads** (Healthy): Healthy depth, strategies can size up safely.
- **OI / Price Divergence** (Fragile positioning): OI rising while price stalls or falls = fragile positioning.
- **Depth Withdrawal** (Cascade setup): Market makers pulling bids/asks ahead of vol events.
- **Post-Cascade Impaired Depth** (Reduce size): Depth hasn't recovered post-event; reduce size, avoid breakout plays.

## 10 — Institutional Flow (Weeks–Months, Structural floor)
ETF and 401(k) access made institutional flows a trackable regime driver. Sustained inflows set structural floors defending specific cost-basis levels — $80K BTC was the 2025 ETF floor.
- **ETF Inflow Accumulation** (Accumulate): >$500M/week sustained inflows = institutional buying.
- **ETF Outflow / Redemption** (De-risk): Spike in redemptions = institutional de-risking. Reduce exposure.
- **ETF Cost Basis Proximity** (Floor defense): When BTC approaches average ETF cost basis, institutional holders defend aggressively.
- **401(k) / Pension Allocation** (Structural floor): Slow but large structural inflows set multi-month floors.

## 11 — Security / Black Swan (Hours–Days, Short then long reversal)
Exchange hacks, protocol exploits, stablecoin depegs trigger measurable, repeatable patterns. The 2025 Bybit hack ($1.46B stolen) created a forensic regime — immediate OI unwind, self-custody withdrawals, then institutional reaccumulation.
- **Exchange Hack / Exploit** (Short → Long): Immediate OI unwind, users withdraw to self-custody. Eventually accelerates regulated-wrapper adoption.
- **Protocol Exploit** (Sector contagion): DeFi bridge or stablecoin exploit triggers sector-specific contagion.
- **Stablecoin Depeg Cascade** (Systemic): Systemic fear, all assets drop together.
- **Adoption Paradox** (Long reversal): Security shocks often accelerate institutional adoption of regulated wrappers post-event.

## 12 — Geopolitical / Policy Shock (Hours–Weeks, Both)
Policy and geopolitics produce their own forensic regimes — pro-crypto executive orders trigger euphoric OI build, tariff escalations trigger macro cascades.
- **Pro-Crypto Policy** (Euphoric): Immediate OI build, euphoric positioning, basis spikes.
- **Trade War / Tariff Escalation** (Risk-off cascade): Crypto correlates with equities during the cascade.
- **Central Bank Rate Signals** (Risk on/off): Fed pivot = BTC risk-on rally. Tightening = risk-off across all assets.
- **Country Ban / Adoption** (Fade within days): Sharp single-day moves, typically fade within days.

## 13 — Volatility Regime (Days–Weeks, Risk sizing overlay)
Realized vs implied vol is a standalone basket. The most dangerous setup is calm-looking compressed vol that masks leverage buildup — the dry tinder before every cascade.
- **Compressed Vol** (Most dangerous): Low ATR (~30% annualized) — appears calm but masks leverage buildup.
- **Vol Expansion / Breakout** (Trade direction): Trade the direction of the breakout with momentum.
- **Vol Mean Reversion** (Fade spike): After a spike, fade back to mean; short straddle equivalent on perps.
- **Vol Risk Premium** (Fade fear): Implied > realized = market overpaying for protection. Fade the fear.

## 14 — Technical / Structural (Hours–Days, Universal overlay)
Price-structure setups that activate across any regime — not a market state on its own, but a universal overlay. Confirmation comes from layering derivatives (funding, OI) on the price signal.
- **Key MA Breakdown / Reclaim** (Short/Long): 200MA reclaim = institutional re-entry; breach = institutional selling.
- **Breakout from Compression** (Long or Short): Bollinger Band squeeze + rising OI = impending vol expansion.
- **Range High/Low Fade** (Mean reversion): Defined multi-week range; fade extremes with tight stops. Highest hit rate during low-vol/chop.
- **Trend Exhaustion / Overextension** (Counter-trend): RSI >80 or <20 + funding extreme + high OI = fade opportunity.

## Design principle
Each basket implies a different set of coins, leverage levels, holding durations, and funding cost tolerance. Mixing them turns one strategy into noise inside another — bull-run logic firing during a liquidation cascade, range-fade dying on a breakout. Treating regimes as distinct strategies, gated by detection, prevents that.
