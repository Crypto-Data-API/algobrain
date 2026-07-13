---
title: "ML-Driven DeFi Risk Models"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [crypto, defi, machine-learning, risk-management, ai-trading]
aliases: ["ML Risk Curators", "DeFi Credit Scoring", "AI Risk Parameters", "ML Lending Risk"]
domain: [market-microstructure, risk-management]
difficulty: advanced
related: ["[[aave]]", "[[morpho]]", "[[defai]]", "[[risk-management]]", "[[decentralized-ai]]", "[[ai-finance]]", "[[ai-trading-agents]]", "[[artificial-intelligence]]"]
---

# ML-Driven DeFi Risk Models

**ML-driven DeFi risk models** are the machine-learning systems — mostly run by professional "risk curator" firms — that set and adjust the key parameters of DeFi lending protocols: collateral factors, borrow caps, liquidation thresholds, interest-rate curves, and pool whitelists. They are the most mature, most revenue-generating, and most under-narrated production use of ML in DeFi today. While retail attention goes to AI agent tokens and autonomous trading, the firms actually earning fees from ML-in-DeFi are doing it by running risk curation for [[aave|Aave]], [[morpho|Morpho]], and their peers.

## Why DeFi Lending Needs ML Risk Parameters

Every DeFi lending protocol faces the same core problem: what collateral factor to set for a given asset, how much to cap its supply, and how to adjust those parameters as market conditions change. These parameters are the difference between a protocol that absorbs losses gracefully during a market shock and one that experiences bad debt because its risk model was too permissive.

Historically, these parameters were set by governance votes informed by spreadsheet analyses and lightly modeled scenarios. That approach works for a handful of assets in calm markets. It fails when:

- A protocol adds dozens of long-tail assets that require per-asset risk analysis
- Market conditions shift faster than governance cycles can respond (minutes vs weeks)
- Correlated risks between assets require joint modeling that spreadsheets don't capture
- Liquidation dynamics depend on on-chain liquidity that changes continuously

ML — supervised forecasting, copula-based correlation models, agent-based liquidation simulations, deep volatility models — is the obvious tool. The leading DeFi protocols have mostly converged on the pattern: **governance delegates parameter setting to ML-running curator firms, with on-chain enforcement of the parameters they recommend**.

## The Risk Curator Model

[[morpho|Morpho]] was the first major lending protocol to formalize this, through its "curator" system: anyone can launch an isolated market on Morpho with whatever parameters they choose, and professional curators (Gauntlet, Block Analitica, Steakhouse, Re7 Labs, and others) publish their parameter recommendations that users can subscribe to. The curator's reputation — and business — depends on whether their recommendations avoid bad debt while generating competitive yields. This pattern has since been adopted or adapted by [[aave|Aave]] (through its own risk service providers), Spark, and several smaller protocols.

The curator model has four important structural properties worth naming:

1. **Professionalization of risk management** — parameter setting moves from unpaid governance to paid professional firms, which makes the quality ceiling much higher
2. **Competition over accuracy** — curators compete to deliver better risk-adjusted returns, creating an economic incentive to invest in better ML
3. **Transparent track records** — curator performance is measurable on-chain (bad debt incurred, liquidations processed), which provides clean data for comparing providers
4. **Revenue capture** — curators earn fees for their service, making this the first DeFi category where ML-running firms have a clear business model with measurable product-market fit

## What the ML Actually Does

Concretely, a risk curator running an ML stack for a lending protocol typically operates several connected models:

### 1. Volatility and Drawdown Forecasting

Per-asset models that forecast realized volatility and maximum drawdown over relevant time horizons. These set collateral factors: a riskier asset gets a lower collateral factor, which limits user leverage and reduces the protocol's exposure to liquidation cascades. Model families include GARCH variants, stochastic volatility models, and neural volatility forecasters.

### 2. Liquidity Depth Monitoring

Models that estimate how much of an asset can be liquidated without catastrophic slippage. This sets borrow caps: if a protocol can only liquidate $10M of an asset before slippage exceeds the liquidation penalty, the protocol cannot safely allow total borrows that would require liquidating more than $10M in a single event. On-chain DEX data is the primary input.

### 3. Correlation and Contagion Models

Models that estimate how losses in one asset propagate to others, especially during stress events. This matters for cross-asset liquidation cascades: if ETH liquidations trigger stETH liquidations that trigger other LST liquidations, the protocol needs joint-loss modeling, not per-asset modeling. Copula methods and historical stress replay are the standard tools here.

### 4. Agent-Based Liquidation Simulators

Simulations that replay historical stress events (March 12 2020, November 2022, various 2024 events) through the protocol's parameter set, measuring whether liquidations would have processed cleanly or produced bad debt. This is the category where [[decentralized-ai|decentralized AI]] ideas intersect most directly with lending — on-chain replay data is public, so simulations can be reproduced by anyone.

## Leading Risk Curator Firms

| Firm | Protocols Served | Specialization |
|------|------------------|----------------|
| **Gauntlet** | Aave, Compound, Morpho, Aerodrome, many others | Agent-based simulation, parameter recommendations |
| **Block Analitica** | Morpho, MakerDAO spark | Data-driven parameter optimization |
| **Chaos Labs** | Aave, GMX, dYdX | Economic security simulation and monitoring |
| **Re7 Labs** | Morpho, others | Curator-focused parameter management |
| **Steakhouse Financial** | Morpho, Maker | Research-driven risk curation |

Gauntlet is the pioneer and largest; the others have followed or specialized in specific protocols. Collectively, these firms are the closest thing DeFi has to a professional asset-liability management industry, and their ML stacks are where most real money-handling ML in DeFi currently runs.

## Why This Category Is Under-Narrated

If risk curation is the most economically serious ML application in DeFi, why is it under-discussed in AI×crypto conversations? A few honest reasons:

- **It's not speculative**. Risk curators don't have tokens that pump on AI narrative. They earn fees for a service.
- **It's institutional, not retail**. Users interact with it indirectly (as an Aave depositor you benefit from the risk service but never see it).
- **The best firms don't publicize their ML**. Gauntlet and peers describe their models as "agent-based" or "simulation-driven" rather than leaning into "AI" branding, because their customers are sophisticated and prefer accurate framing.
- **It competes with DeFi's populist mythology**. DeFi's self-image is permissionless and trustless; professional risk curators are neither, and the narrative avoids emphasizing how much the category depends on them.

The practical result is that one of DeFi's most important and most ML-driven categories gets less attention than speculative agent tokens. This is a narrative failure, not a technical one.

## Risks and Limitations

ML-driven risk curation is not a silver bullet. Honest failure modes worth naming:

- **Models trained on calm regimes underestimate tail risk**. Every major stress event in DeFi history has exposed risk parameters that looked safe in backtests.
- **Adversarial borrowers can game the models**. A borrower who understands the parameter-update cadence can time their actions to extract value before parameters adjust.
- **Curator competition is a race to the bottom in some dimensions**. If one curator offers more aggressive parameters, another has to match or lose subscribers — which can drive protocol-level risk up even as individual curator models improve.
- **Governance lag**. Even the best ML recommendation is useless if protocol governance takes a week to approve the parameter change.

## See Also

- [[aave]] — Major lending protocol using risk service providers
- [[morpho]] — Formalized the risk curator model
- [[ai-finance]] — Broader AI in finance context
- [[risk-management]] — Classical risk management concepts
- [[defai]] — DeFi + AI parent narrative
- [[decentralized-ai]] — Broader AI×crypto context
- [[ai-trading-agents]] — Adjacent autonomous-agent concept
- [[artificial-intelligence]] — AI section hub

## Sources

- Gauntlet, Chaos Labs, Block Analitica, Steakhouse, and Re7 Labs public risk methodology and parameter-recommendation documentation (as of 2026)
- Morpho curator documentation (isolated markets and curator subscription model)
- Aave risk service provider governance proposals and dashboards
