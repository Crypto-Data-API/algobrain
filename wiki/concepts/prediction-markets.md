---
title: "Prediction Markets"
type: concept
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [prediction-markets, crypto, defi, market-microstructure, behavioral-finance]
aliases: ["Prediction Markets", "Event Markets", "Information Markets", "Betting Markets", "Event Contracts"]
domain: [market-microstructure, behavioral-finance]
prerequisites: ["[[order-types]]"]
difficulty: beginner
related: ["[[polymarket]]", "[[kalshi]]", "[[ai-prediction-markets]]", "[[prediction-market-strategies]]", "[[polymarket-vs-kalshi]]", "[[behavioral-finance-overview]]", "[[market-efficiency]]"]
---

# Prediction Markets

**Prediction markets** (also called event markets, information markets, or event contracts) are exchange-traded markets where participants buy and sell contracts whose payoff is tied to the outcome of a real-world event. Each contract typically resolves to $1 (if the event occurs) or $0 (if it does not), and the market price at any point reflects the crowd's implied probability of that outcome. A contract trading at $0.70 implies the market collectively estimates a 70% chance the event will happen.

## Why They Matter

Prediction markets derive their forecasting power from two reinforcing mechanisms:

1. **Wisdom of crowds** — diverse participants aggregate private information into a single price signal
2. **Financial incentives for accuracy** — traders risk real capital, incentivizing genuine belief revelation over socially desirable signaling, and intensive research to gain an edge

This is why [[polymarket|Polymarket's]] 2024 US election odds proved more accurate than most traditional polls: polls ask what people *think*; prediction markets ask people to put *money* behind their beliefs. The epistemological argument is that prediction market probabilities could become as standard as stock quotes for navigating uncertainty in politics, business, and policy-making. (Source: [[polymarket-wiki-guide]])

## How They Work

### Core Mechanic

1. A market poses a specific, verifiable question (e.g., "Will the Fed cut rates in June 2026?")
2. Users buy "Yes" or "No" shares priced between $0.01 and $0.99
3. The price equals the implied probability (a "Yes" share at $0.65 = 65% probability)
4. Positions can be traded at any time as new information shifts odds
5. At resolution, winning shares pay $1; losing shares expire worthless

### Market Types

| Type | Structure | Example |
|------|-----------|---------|
| **Binary** | Yes/No on single outcome | "Will BTC exceed $100K by Dec 2026?" |
| **Multi-outcome** | Multiple mutually exclusive options | "Who wins the 2028 presidential election?" |
| **Scalar/Range** | Continuous outcome mapped to a range | "What will CPI be in Q3 2026?" |

### Resolution Mechanisms

| Mechanism | Used By | Pros | Cons |
|-----------|---------|------|------|
| **Centralized** | [[kalshi]] | Fast, unambiguous | Single point of failure; trust requirement |
| **Optimistic Oracle** (UMA) | [[polymarket]] | Decentralized; censorship-resistant | Vulnerable to token-holder manipulation (see Zelenskyy suit incident) |
| **Human jury** | Augur (historical) | Democratic | Slow, expensive, low participation |
| **LLM-based** | Emerging (Olas Predict) | Scalable, fast | Calibration concerns; adversarial inputs |

## Major Platforms (2026)

| Platform | Type | Settlement | Regulation | Fees | Valuation |
|----------|------|-----------|------------|------|-----------|
| [[polymarket|Polymarket]] | Decentralized (Polygon) | USDC | CFTC-compliant (via QCEX, 2025) | 0% | $9B |
| [[kalshi|Kalshi]] | Centralized | USD | CFTC-regulated since founding | Yes | ~$2B |
| **Azuro** | Decentralized | Crypto | Unregulated | Varies | — |
| **Manifold Markets** | Play-money | N/A | N/A | Free | — |

See [[polymarket-vs-kalshi]] for a detailed comparison of the two dominant platforms.

(Source: [[polymarket-wiki-guide]])

## Prediction Market Theory

### Efficient Information Aggregation

Prediction markets are a practical application of [[market-efficiency|market efficiency]] theory applied to event outcomes rather than asset prices. When diverse participants trade on private information:
- Optimists buy "Yes" and push prices up
- Pessimists buy "No" and push prices down
- The equilibrium price approximates the true probability

This works best when markets are liquid, diverse, and participants have genuine information heterogeneity.

### Known Biases

Despite their accuracy advantages, prediction markets exhibit systematic biases:

- **Favorite-longshot bias** — longshot outcomes tend to be overpriced (too many people buy "Yes" on exciting but unlikely events). This is the bias Vitalik Buterin exploited to make $70K on Polymarket in 2024. (Source: [[polymarket-wiki-guide]])
- **Recency bias** — markets overweight recent news relative to base rates
- **Anchoring** — market prices can be slow to move from initial levels when early liquidity sets the tone
- **Thin-market noise** — illiquid markets produce noisy probability estimates

### Comparison to Polls and Expert Forecasts

| Dimension | Prediction Markets | Polls | Expert Forecasts |
|-----------|-------------------|-------|-----------------|
| **Incentive alignment** | High (real money) | Low (no stake) | Medium (reputation) |
| **Update speed** | Real-time | Days/weeks | Irregular |
| **Aggregation method** | Price discovery | Statistical sampling | Subjective synthesis |
| **Track record (elections)** | Strong (2024 validated) | Mixed | Mixed |
| **Sample** | Self-selected traders | Designed sample | Small N |

## Regulatory Landscape (2026)

Prediction markets sit in a contested regulatory space between derivatives exchanges and gambling:

- **US federal**: The [[cftc|CFTC]] treats prediction markets as derivatives; filed amicus briefs supporting this classification
- **US state**: 20+ federal lawsuits across 7 states argue prediction markets are gambling under state gaming laws
- **Historical**: Polymarket fined $1.4M by CFTC in 2022; subsequently acquired CFTC-licensed QCEX in 2025 to re-enter US legally
- **International**: Legal gray area in most jurisdictions; Polymarket's global user base operated without formal licensing in most countries until 2025

(Source: [[polymarket-wiki-guide]])

## Insider Trading and Manipulation Risks

Prediction markets lack the insider trading enforcement mechanisms of traditional securities markets. Notable concerns:

- **No formal insider trading prevention** — individuals with material non-public information can bet on outcomes they have advance knowledge of
- **Documented suspicious activity** on Polymarket around geopolitical events (Russo-Ukrainian War, Venezuela strikes, Israeli operations, OpenAI corporate events)
- **Oracle manipulation** — the Zelenskyy suit controversy (July 2025) showed that decentralized oracle resolution can be captured by wealthy token holders
- **Wash trading** — on-chain settlement makes volume verification possible but does not prevent coordinated manipulation across accounts (see "Theo" using 11 accounts)

(Source: [[polymarket-wiki-guide]])

## AI Integration

[[ai-prediction-markets|AI and prediction markets]] are deeply intertwined as of 2026:
- AI agents actively trade on Polymarket (LLM-powered bots, OpenClaw framework)
- Prediction markets host 133+ AI-specific markets ($15M+ volume)
- Prediction market prices are used as calibration signals for AI forecasting models
- [[palantir-technologies|Palantir]] partnership deploys Vergence AI for integrity monitoring

See [[ai-prediction-markets]] for the full treatment.

## See Also

- [[polymarket]] — Largest decentralized prediction market ($9B valuation)
- [[kalshi]] — Largest regulated prediction exchange (~$2B valuation)
- [[polymarket-vs-kalshi]] — Head-to-head comparison
- [[prediction-market-strategies]] — Trading strategies specific to prediction markets
- [[ai-prediction-markets]] — AI integration with prediction markets
- [[behavioral-finance-overview]] — Biases that create prediction market edges

## Sources

- [[polymarket-wiki-guide]] — Primary source (compiled research, 43 citations)
