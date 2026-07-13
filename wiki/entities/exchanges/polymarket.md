---
title: "Polymarket"
type: entity
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [crypto, defi, prediction-markets, regulation]
aliases: ["Polymarket", "POLY"]
entity_type: exchange
founded: 2020
headquarters: "New York City, USA"
website: "https://polymarket.com"
related: ["[[kalshi]]", "[[prediction-markets]]", "[[polygon]]", "[[shayne-coplan]]", "[[ai-prediction-markets]]", "[[prediction-market-strategies]]", "[[polymarket-vs-kalshi]]", "[[market-efficiency]]", "[[wisdom-of-crowds]]", "[[event-driven]]", "[[arbitrage]]", "[[usdc]]"]
---

# Polymarket

**Polymarket** is the world's largest decentralized [[prediction-markets|prediction market]] platform, founded in 2020 by [[shayne-coplan|Shayne Coplan]]. Users trade binary "Yes" or "No" shares on real-world event outcomes — from elections and geopolitics to crypto prices, AI milestones, and pop culture — all denominated in USDC on the [[polygon|Polygon]] blockchain. As of October 2025, Polymarket carries a $9 billion valuation following a $2 billion strategic investment from Intercontinental Exchange (ICE), the parent company of the NYSE. (Source: [[polymarket-wiki-guide]])

## How It Works

### Core Mechanic

Each market poses a binary question. Users buy "Yes" or "No" shares priced between $0.01 and $0.99. The price reflects the market's collective implied probability of that outcome. If the event resolves "Yes," each Yes share pays $1 USDC; otherwise it expires worthless. Positions can be bought and sold at any time as odds shift, allowing traders to lock in profits or cut losses before resolution. (Source: [[polymarket-wiki-guide]])

### Price as Implied Probability

The central insight for a trader is that **a Polymarket price is a probability quote, not a dollar price of an asset**. A "Yes" share trading at $0.62 means the market collectively assigns ~62% probability to that outcome. This makes Polymarket a real-money probability oracle that updates continuously — far more responsive than periodic polls or surveys.

| Yes price | Implied probability | Yes payoff if correct | Yes loss if wrong |
|-----------|---------------------|-----------------------|-------------------|
| $0.10 | 10% | +$0.90 per share (9:1) | -$0.10 |
| $0.50 | 50% | +$0.50 per share (1:1) | -$0.50 |
| $0.90 | 90% | +$0.10 per share (1:9) | -$0.90 |

Because Yes + No must sum to ~$1.00 (minus any spread), the two sides are mirror positions. The market is a [[wisdom-of-crowds\|crowd-aggregated]] forecast that a trader can either *trust* (treat as signal) or *fade* (treat as mispriced) — see [[#Using Polymarket as a Signal Source]] and [[prediction-market-strategies]].

### Why Real-Money Markets Aggregate Information

Real-money prediction markets tend to outperform polls and pundits because participants are financially incentivized to be right rather than loud. Informed traders move price toward the true probability to capture profit; uninformed noise tends to cancel. This is the practical mechanism behind [[wisdom-of-crowds]] and a live test of [[market-efficiency]] applied to discrete events. The caveat: efficiency degrades in thin, low-volume markets and in markets vulnerable to manipulation or insider information (see [[#Controversies and Risks]]).

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Settlement chain** | [[polygon|Polygon PoS]] (Layer-2) | Scalable, low-fee transaction processing; millions of daily trades |
| **Token standard** | Conditional Token Framework (ERC-1155) | Binary outcome tokens backed by USDC collateral |
| **Order matching** | Hybrid CLOB | Off-chain order book for fast matching; on-chain settlement |
| **Resolution** | UMA Optimistic Oracle | Decentralized outcome verification; 2-hour challenge window; $750 USDC dispute bond |

**Order types:** GTC (Good-Till-Cancelled), GTD (Good-Till-Date), FOK (Fill-Or-Kill), FAK (Fill-And-Kill). (Source: [[polymarket-wiki-guide]])

### Settlement and Fees

- All trades denominated in **USDC** (USDT, SOL, and other assets auto-converted on deposit)
- **Zero trading fees** on transactions — a key differentiator from [[kalshi]] and traditional platforms
- Winning tokens redeem for $1 USDC; losing tokens expire worthless
- All trades settle transparently on-chain
- As of December 2024, Polymarket began resolving certain disputes through its own internal mechanism for controversial bets (Source: [[polymarket-wiki-guide]])

## Market Categories

Polymarket hosts markets across a broad range of topics:

- **Politics & Public Policy** — election results, legislative outcomes, government policy, geopolitics
- **Crypto & Finance** — [[bitcoin|Bitcoin]]/[[ethereum|Ethereum]] price thresholds, interest rate decisions, equity indices, macro data releases (CPI, GDP)
- **Sports** — tournament winners, game outcomes, player statistics
- **AI & Technology** — AGI timelines, LLM model releases, [[openai|OpenAI]]/[[anthropic|Anthropic]] announcements
- **Geopolitics** — military conflicts, diplomatic outcomes, sanctions
- **Culture & Entertainment** — award show winners, pop culture events
- **Weather & Science** — natural disaster occurrences, scientific discoveries

As of April 2026, Polymarket hosts **133 active LLM/AI-specific prediction markets** with over $15 million in trading volume. (Source: [[polymarket-wiki-guide]])

## Key Milestones

| Date | Event |
|------|-------|
| **2020** | [[shayne-coplan|Shayne Coplan]] founds Polymarket during COVID-19 pandemic |
| **2022** | [[cftc|CFTC]] fines Polymarket $1.4M for operating unregistered derivatives exchange; ordered to block US users |
| **2024 (election)** | $3.6B+ in election betting volume; odds prove more accurate than traditional polls; mainstream media adoption |
| **Nov 2024** | FBI raids Coplan's Manhattan apartment; seizes electronics; no charges filed; investigation later closed |
| **Mid-2025** | $200M raise led by Peter Thiel's Founders Fund; $1B valuation; named official prediction market partner of X (Twitter) |
| **May 2025** | 15.9M monthly visits — surpasses FanDuel and DraftKings |
| **Jul 2025** | Zelenskyy suit controversy — $58M bet; UMA oracle reverses decision twice; manipulation allegations |
| **Jul 2025** | Acquires QCEX (CFTC-licensed derivatives exchange) for $112M; enables legal US relaunch |
| **Aug 2025** | Donald Trump Jr. joins as advisor (via 1789 Capital) |
| **Oct 2025** | ICE invests $2B at $9B valuation; becomes global distributor of Polymarket event data |
| **Mar 2026** | Partnership with Palantir and TWG AI — Vergence AI engine for sports integrity monitoring |
| **2026** | 20+ federal lawsuits across 7 US states challenging prediction markets as gambling |

(Source: [[polymarket-wiki-guide]])

## Notable Traders

### The $85 Million "Theo" Trade

The most famous individual trade in Polymarket history. A French trader identified as "Theo" used up to 11 accounts to bet heavily on Donald Trump's 2024 victory. Chainalysis analysis confirmed total earnings exceeding **$85 million** — far more than the initially reported $48M. The day before the election, his known accounts faced ~$3M in unrealized losses as odds tightened. His stated rationale was strong personal conviction, not manipulation. (Source: [[polymarket-wiki-guide]])

### Vitalik Buterin's "Boring" Strategy

[[ethereum|Ethereum]] co-founder Vitalik Buterin made **$70,000** in 2024 by fading long-shot bets — taking the other side of high-risk positions where the public overestimates flashy outcomes. He previously made $58,000 on the 2020 US election. The strategy is essentially acting as an insurance provider against low-probability events. (Source: [[polymarket-wiki-guide]])

### Top All-Time Traders

| Trader | Focus | Biggest Win | Total Profit |
|--------|-------|------------|-------------|
| 1j59y6nk | Sports (Baseball/Football) | $90K | ~$1.4M |
| Erasmus | Politics | $95K | ~$1.3M |
| HyperLiquid0xb | Sports (Baseball) | $755K | ~$1.4M |
| WindWalk3 | Politics (RFK Jr. markets) | $1.1M | ~$1.1M+ |
| Bama124 | Politics | $593K | ~$1M+ |

(Source: [[polymarket-wiki-guide]])

## How Traders Use Polymarket

There are two distinct ways to use Polymarket: as a **venue to trade** and as a **data source to inform trades elsewhere**.

### Trading Approaches (on-platform)

| Approach | Description | Edge source |
|----------|-------------|-------------|
| **Conviction / directional** | Buy Yes or No when you believe the true probability differs from the quoted price | Superior information or analysis |
| **Fading long shots** | Sell (or take No on) overpriced flashy outcomes the public overbets; Vitalik Buterin's documented approach | [[behavioral-finance\|Behavioral]] overpricing of salient events |
| **Mean reversion on overreaction** | Trade against knee-jerk price spikes after news, betting the move overshoots | Overreaction / emotional mispricing |
| **Resolution arbitrage** | When Yes + No < $1.00 net of fees, buy both for a locked profit at resolution | Pricing inefficiency / [[arbitrage]] |
| **Cross-venue arbitrage** | Exploit price gaps between Polymarket and [[kalshi]] on equivalent questions | Fragmented liquidity across venues |
| **Event-driven / news trading** | Position ahead of or react faster to scheduled events (CPI, elections, rulings) | Speed and interpretation; see [[event-driven]] |
| **Liquidity provision** | Provide depth / market-make on the [[#Technology Stack\|hybrid CLOB]] | Spread capture (with inventory and resolution risk) |

> Polymarket charges **zero trading fees**, which materially improves the math for high-frequency, arbitrage, and market-making approaches relative to fee-charging venues like [[kalshi]].

### Using Polymarket as a Signal Source

Even traders who never place a bet use Polymarket prices as a live, real-money probability feed for decisions in other markets:

- **Macro / rates positioning** — interest-rate and CPI markets give a continuously-updating implied probability of Fed decisions and data prints, useful for [[bonds\|rates]] and equity-index traders alongside Fed-funds futures
- **Event risk hedging** — election, geopolitical, and policy markets quantify binary risk that can be cross-hedged in equities, FX, or crypto
- **Crypto thresholds** — [[bitcoin\|BTC]]/[[ethereum\|ETH]] price-threshold markets reveal the crowd's implied distribution of near-term price outcomes
- **Sentiment timing** — sharp moves in a market often *lead* mainstream news, acting as an early-warning signal
- **AI / tech milestones** — AGI-timeline and model-release markets price expectations that move adjacent equities ([[#AI and LLM Integration]])

The discipline: treat the price as a *prior*, then ask whether you have an information or analysis edge that justifies a different probability. If not, the market's number is usually the best available estimate.

### Data Access for Systematic Users

For programmatic consumption, Polymarket exposes a full API surface (see [[#Developer Ecosystem]]): the REST/WebSocket feeds and Gamma API provide market metadata, order-book depth, and historical prices suitable for backtesting and for piping prediction-market probabilities into a broader trading model. All trades also settle transparently on-chain via [[polygon\|Polygon]] block explorers, enabling independent verification and whale tracking.

## AI and LLM Integration

Polymarket sits at the intersection of [[prediction-markets|prediction markets]] and [[artificial-intelligence|artificial intelligence]]. See [[ai-prediction-markets]] for the full concept page.

- **LLM-Powered Trading Bots** — Claude, GPT-4, and Grok used to parse news, assess probabilities, generate trade signals. Core hypothesis: AI agents exploit emotional mispricings more rationally than humans. (Source: [[polymarket-wiki-guide]])
- **OpenClaw / Polyclaw** — By early 2026, the most mature open-source AI bot framework for Polymarket (by Chainstack); browses markets, executes trades, runs LLM-powered hedge discovery via CLOB API
- **Solana AI Agents** — Polymarket and [[kalshi]] markets accessible on Solana through Jupiter's `sol predict` infrastructure
- **60-Day LLM Experiment** — Paper trading showed AI outperforms on price threshold questions (technical momentum), humans retain edge on event-based questions requiring insider knowledge
- **AI Ensemble Testing** — Strategy Arena pitted 9 AI models against Polymarket human odds on 49 crypto markets; AI outperformed on quantitative questions, lagged on event-based
- **Palantir Integrity** — Vergence AI engine monitors real-time trades, detects manipulation, insider trading, and coordinated activity

(Source: [[polymarket-wiki-guide]])

## Controversies and Risks

### Insider Trading

No formal mechanism prevents individuals with material non-public information from betting. Suspicious activity observed around:
- Russo-Ukrainian War events
- 2026 US strikes in Venezuela
- Israeli military operations
- 2026 Israeli-US strikes on Iran
- [[openai|OpenAI]] corporate events

US Representative Ritchie Torres has described this as a "legal grey area." (Source: [[polymarket-wiki-guide]])

### Oracle Manipulation

The Zelenskyy suit controversy (July 2025) exposed a fundamental vulnerability: wealthy UMA token holders can potentially influence dispute resolution outcomes. The UMA oracle reversed its initial decision twice under alleged pressure, raising questions about the reliability of "decentralized" resolution for high-stakes markets. (Source: [[polymarket-wiki-guide]])

### Regulatory Status

| Year | Event |
|------|-------|
| 2022 | $1.4M CFTC fine; consent decree to block US users |
| 2024 | FBI raid on CEO (no charges filed) |
| 2025 | CFTC concluded investigation; QCEX acquisition enables legal US operations |
| 2026 | 20+ state lawsuits classifying prediction markets as gambling; CFTC files amicus briefs supporting Polymarket as a federally regulated derivatives exchange |

(Source: [[polymarket-wiki-guide]])

### Trader Risk Summary

Beyond the headline controversies, these are the practical risks a Polymarket trader should price in:

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Resolution / oracle risk** | UMA Optimistic Oracle can be disputed or, as in the Zelenskyy case, reversed; ambiguous question wording causes contested outcomes | Read the exact resolution criteria; avoid vaguely-worded markets |
| **Insider / asymmetric information** | No mechanism blocks informed insiders; you may be trading against someone who *knows* the outcome | Be cautious in markets where private information likely exists |
| **Liquidity / slippage** | Thin markets have wide spreads and poor depth; large orders move price | Size to available depth; check order-book before entering |
| **Counterparty / smart-contract** | Funds held in on-chain contracts on [[polygon]]; bridge, contract, or [[usdc]] de-peg risk | Treat as crypto-platform risk, not bank-grade custody |
| **Regulatory / access** | Legal status varies by jurisdiction; US access historically restricted then re-enabled via QCEX license | Confirm legality in your jurisdiction |
| **Capital lockup** | Capital is tied up until resolution unless you exit at market | Account for time value; long-dated markets lock funds for months |

## POLY Token

As of April 2026, the POLY token has been confirmed but not launched:

- **No official TGE date** — launch tied to completion of US platform relaunch
- **Airdrop confirmed** — CMO confirmed on Degenz Live podcast (October 2025)
- **Planned uses** — governance voting, market security staking incentives
- **Community sentiment** — ~79% of Polymarket bettors expect token before end of 2026
- **Farming** — active trading volume and market creation are primary airdrop positioning strategies

(Source: [[polymarket-wiki-guide]])

## Developer Ecosystem

| API | Purpose |
|-----|---------|
| **REST API & WebSocket** | Market data, order book depth, trade history, user positions |
| **CLOB API** | Direct order submission via EIP-712 signed messages |
| **Gamma API** | Market metadata, categories, tags |
| **Python SDK** | Official Python client library |
| **TypeScript SDK** | Official TypeScript client library |

- **170+ third-party tools**, bots, and analytics dashboards built around the platform
- **$1 million Builders Incentive Program** funds new developer applications
- On-chain trade data fully accessible via Polygon block explorers

(Source: [[polymarket-wiki-guide]])

## See Also

- [[prediction-markets]] — The broader concept
- [[kalshi]] — Main competitor (CFTC-regulated, centralized)
- [[polymarket-vs-kalshi]] — Head-to-head comparison
- [[prediction-market-strategies]] — Trading strategies for prediction markets
- [[ai-prediction-markets]] — AI integration with prediction markets
- [[shayne-coplan]] — Founder
- [[polygon]] — Underlying blockchain
- [[wisdom-of-crowds]] — Why real-money markets aggregate information
- [[market-efficiency]] — The efficiency hypothesis applied to event markets
- [[event-driven]] — Trading scheduled and unscheduled events
- [[arbitrage]] — Resolution and cross-venue arbitrage approaches
- [[usdc]] — Settlement stablecoin

## Sources

- [[polymarket-wiki-guide]] — Primary source (compiled research, 43 citations)
