---
title: "DePIN"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
tags: [crypto, defi, real-world-assets, on-chain]
aliases: ["Decentralized Physical Infrastructure Networks", "Decentralised Infrastructure"]
domain: [crypto, market-microstructure]
difficulty: intermediate
---

# DePIN

**Decentralized Physical Infrastructure Networks (DePIN)** use token incentives to crowdsource the buildout and operation of real-world hardware infrastructure — compute, wireless connectivity, energy grids, data storage, and sensor networks. Instead of a corporation owning the infrastructure and capturing its economics, a protocol issues tokens to individuals who contribute hardware, and those contributors earn yield proportional to their service delivery. The category includes Helium (wireless hotspots), Filecoin (storage), Render Network (GPU compute), and Hivemapper (mapping data), among hundreds of others.

## How It Works

A DePIN protocol has four components:

1. **Physical hardware contributors** — individuals or companies that deploy hardware (routers, storage nodes, GPUs, sensors) and run protocol software.
2. **Token emissions** — the protocol mints tokens and distributes them to hardware operators in proportion to verified service delivery. This is the bootstrap subsidy: the token is worthless if the network is empty, so early participants are overpaid to build critical mass.
3. **Demand-side revenue** — as the network matures, real customers pay tokens (or fiat converted to tokens) for the service: bandwidth, storage space, rendering jobs, map updates.
4. **On-chain verification** — service delivery is verified by oracles, zero-knowledge proofs, or peer-to-peer attestation, so the protocol can programmatically reward genuine contributors and slash or ignore bad actors.

**The economic flywheel:** Token emissions attract operators → operators build supply → supply attracts customers → customer revenue supports token value → higher token price attracts more operators. The failure mode is the reverse: if token price drops faster than supply builds, operators leave, degrading the network, further depressing the token.

## Concrete Examples

- **Helium (HNT/MOBILE/IOT, 2013–):** Crowdsourced LoRaWAN and 5G hotspot network. At peak, over 1 million hotspots globally. Migrated from its own L1 to Solana in 2023. Real telecom carrier (T-Mobile) partnered for MOBILE use cases. Token emission schedule front-loads early operators.
- **Filecoin (FIL, 2017 mainnet 2020):** Decentralised storage. Operators prove they store data via verifiable Proof-of-Spacetime. Competes with S3/GCP storage on cost but with lower reliability guarantees for casual users; enterprise use cases require additional replication.
- **Render Network (RENDER, 2020–):** GPU rendering jobs routed to idle consumer GPUs. Migrated from Ethereum to Solana 2023. Real clients include artists and studios who pay RENDER tokens for rendering.
- **Hivemapper (HONEY, 2022–):** Dashcam operators map roads and earn HONEY tokens. Mapping data sold to enterprises and competes with Google Maps on freshness of certain routes.
- **Akash Network (AKT):** Decentralised cloud compute marketplace. Operators list spare compute capacity; buyers bid.

## Trading Relevance

DePIN tokens are a distinct sub-asset class with specific risk drivers:

- **Emission-schedule arbitrage:** Many DePIN protocols front-load emissions heavily in the first 1-3 years. This is a structural sell pressure on the token — early operators have zero cost basis and sell to cover hardware and electricity. Identifying where a DePIN protocol is on its emission curve is a key input to any position.
- **[[vampire-attack-arbitrage]] analogue:** The DePIN bootstrap phase resembles a vampire attack — the protocol overpays for early supply. Traders who provide hardware (or buy tokens at launch) and exit before the emission cliff capture the subsidy window.
- **Revenue-to-emissions ratio (RER):** A DePIN protocol transitions from subsidy-dependent to self-sustaining only when customer revenue exceeds token emissions in dollar terms. Protocols with high RER are better stores of value; low-RER protocols are effectively printing their token to pay suppliers. This ratio is a fundamental valuation metric.
- **Narrative regime correlation:** DePIN tokens trade in the [[gamefi]] / narrative-sector basket during bull markets and re-correlate with broad crypto beta in drawdowns. [[multi-strategy-crypto-portfolio|Multi-sleeve portfolios]] sizing DePIN exposure should model it as a high-beta, high-skew position within the memecoin/convexity sleeve, not as a yield strategy.
- **On-chain verification of supply:** DePIN protocols expose supply metrics on-chain (hotspot counts, storage proofs, GPU jobs completed) that often lead token price. Traders who monitor these metrics via [[on-chain-analysis]] can detect demand/supply divergences before they print in price.

## Related

- [[render-token]] — GPU compute DePIN
- [[filecoin]] — decentralised storage
- [[helium]] — wireless DePIN
- [[zero-knowledge-proofs]] — used in some DePIN verification schemes
- [[real-world-assets]] — DePIN is a sub-category of RWA tokenisation
- [[tokenized-treasuries]] — the yield-bearing RWA category; distinct from DePIN infrastructure
- [[on-chain-analysis]] — supply-side metrics that lead DePIN token prices
- [[vampire-attack-arbitrage]] — bootstrap-phase emission capture analogous to DePIN early operator rewards
- [[layer-1]] — the blockchains DePIN protocols are built on

## Sources

- General crypto/DePIN knowledge; no specific wiki source ingested yet.
