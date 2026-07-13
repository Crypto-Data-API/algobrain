---
title: "Nansen"
type: source
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [data-provider, on-chain-analytics, whale-tracking, crypto, defi]
aliases: ["Nansen.ai"]
source_type: data
source_url: "https://www.nansen.ai"
source_author: "Nansen"
confidence: high
related: ["[[on-chain-analytics]]", "[[information-arbitrage]]", "[[polymarket]]", "[[polymarket-as-crypto-leading-indicator]]", "[[glassnode]]", "[[cryptoquant]]", "[[dune-analytics]]"]
---

Nansen is a Singapore-based on-chain analytics platform founded in 2019, known for its proprietary wallet-labeling database (covering 300M+ labeled addresses) and "Smart Money" cohort tracking across [[ethereum]], [[polygon]], [[solana]], and other major chains. It sits at the institutional end of the on-chain data spectrum, monetizing the work of attributing pseudonymous blockchain addresses to real-world entities — exchanges, market makers, funds, protocol teams, and MEV bots — and turning that labeled graph into actionable trading signals.

## Core product surface

- **Wallet labels** — proprietary identification of CEX addresses, whale wallets, market makers, funds, protocol teams, and MEV bots. The label database is Nansen's central moat: most competitors expose the same raw on-chain data, but few attribute it at comparable scale.
- **Smart Money dashboards** — tracks cohorts (top profitable traders, top funds, top stablecoin holders) and their aggregate flows in and out of tokens, protocols, and chains.
- **Token god mode** — for any token, see top holders, flow in/out, exchange concentration, and the breakdown of holder type (fund vs. retail vs. CEX).
- **Alerts** — webhook, email, and Discord notifications on labeled-wallet activity, enabling event-driven trading integrations.

## Relevance to crypto-trading apps

- **Whale tracking on Polymarket** — [[polymarket]] settles on [[polygon]]; Nansen labels Polymarket-related wallets, enabling identification of large prediction-market positions in real time. This is the operational layer for the "whale-flow signal" thesis in [[polymarket-as-crypto-leading-indicator]] — the same labeling stack that identifies a Solana whale can also surface size accumulating on a specific Polymarket contract.
- **CEX inflow/outflow signals** — large inflows to exchanges typically precede selling pressure on [[bitcoin]] / [[ethereum]]. Nansen's CEX label set is among the most maintained in the industry.
- **Smart Money concentration** — tokens being accumulated by historically-profitable wallets is a documented (if decayed) signal. Useful as a screen, less so as a standalone entry trigger.

## API and data access

- REST API available on institutional tiers (Alpha, VIP, Standard subscriptions)
- Query API for custom on-chain queries against the labeled dataset
- Webhook alerts for real-time integration into trading systems
- Nansen runs a tiered subscription model (a free tier plus paid Standard / VIP / Enterprise-style tiers). Nansen does not consistently publish full pricing publicly and third-party 2026 sources conflict (entry paid tiers reported around ~$99/month, with VIP/institutional tiers running into the high hundreds-to-low thousands per month for full API access). Treat any quoted number as indicative and verify current rates directly before committing

## Comparison to alternatives

| Tool | Strength | Weakness vs Nansen |
|------|----------|---------------------|
| [[dune-analytics]] | Free SQL queries; flexible | No proprietary wallet labels |
| [[glassnode]] | Better macro-aggregated metrics | Less granular wallet tracking |
| [[cryptoquant]] | Strong exchange flow data | Weaker DeFi/NFT coverage |
| [[arkham-intelligence]] | Free tier; entity-based view | Less depth of labels |

## Use cases for a crypto trading app

- Real-time whale alert → directional crypto trade
- Polymarket whale position detection → underlying-asset positioning (per [[polymarket-as-crypto-leading-indicator]])
- Stablecoin flow monitoring → market regime classification (risk-on vs. risk-off based on USDC/USDT minting and exchange flows)
- DEX-vs-CEX flow imbalance → liquidity stress signal
- Pre-listing accumulation detection → screen for tokens being quietly bid by labeled funds

## Limitations

- Wallet labels are proprietary and not always verifiable — users must trust Nansen's attribution
- "Smart Money" cohort can decay; past performance of the cohort is selection-biased (winners are identified after the fact)
- Polymarket-specific labeling lags Polymarket's growth — third-party Polymarket-native analytics dashboards are often more focused for that specific use case
- Subscription cost can dwarf retail-trader budgets at the higher tiers
- Edge from any individual signal compresses as more subscribers buy in — the more popular a Nansen alert becomes, the faster the underlying trade gets front-run

## Notable historical detection cases

- **Pre-FTX collapse (Nov 2022)** — Alameda-related wallet labels enabled forensic tracking of FTT collateralization, contributing to the public narrative once the CoinDesk balance-sheet story broke
- **Pre-Terra/Luna (May 2022)** — 4pool composition deterioration was visible across multiple labeled wallets, with sophisticated holders rotating out before the depeg cascade

Both are also documented in [[information-arbitrage]] §On-chain analytics history.

## Related

- [[on-chain-analytics]]
- [[information-arbitrage]]
- [[polymarket]]
- [[polymarket-as-crypto-leading-indicator]]
- [[glassnode]]
- [[cryptoquant]]
- [[dune-analytics]]
- [[arkham-intelligence]]

## Sources

- Nansen's own product documentation and marketing materials (https://www.nansen.ai)
- [[information-arbitrage]] for the broader information-arbitrage context in which Nansen's data sits
- On-chain analytics platform comparisons, 2026 (Sablier, eco.com, CoinAPI) — used to corroborate that Nansen remains a tiered-subscription provider in 2026; exact pricing not publicly confirmed
