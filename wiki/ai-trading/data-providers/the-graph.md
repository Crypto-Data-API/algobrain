---
title: "The Graph"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, infrastructure, defi]
entity_type: company
website: https://thegraph.com
related:
  - "[[arkham-intelligence]]"
  - "[[nansen]]"
  - "[[glassnode]]"
  - "[[decentralized-ai]]"
  - "[[on-chain-inference]]"
  - "[[defai]]"
  - "[[ai-trading-agents]]"
---

# The Graph

## Overview

Decentralized data indexing protocol for querying blockchain data. The Graph solves a fundamental problem: raw blockchain data is stored in a format optimized for consensus, not for queries. If you want to answer "what were the top 10 Uniswap pools by volume in the last 24 hours?" you would need to run a full node, parse every block, decode every transaction, and build your own database. The Graph does this for you through subgraphs -- open-source indexing specifications that transform raw blockchain events into queryable GraphQL APIs. It is the Google of blockchain data: it indexes and serves what is already public, but makes it actually usable.

## Pricing

- **Free tier**: hosted service with generous query limits for development and testing
- **Decentralized network**: pay per query using GRT tokens (fractions of a cent per query)
- **Subgraph Studio**: free to deploy and test subgraphs
- Cost scales with usage -- low-volume users effectively pay nothing, high-volume dApps pay based on query volume
- Self-hosting is possible but defeats the purpose of the decentralized network

## What You Get (vs Free)

- The free hosted service covers most needs for development and moderate-volume analytics
- Decentralized network provides guaranteed uptime, redundancy, and censorship resistance
- Custom subgraphs: index ANY smart contract event on supported chains (Ethereum, Polygon, Arbitrum, Optimism, Avalanche, and more)
- Pre-built subgraphs exist for major protocols: [[uniswap]], Aave, Compound, MakerDAO, Curve, etc.
- GraphQL API access to indexed data -- filter, sort, paginate, and aggregate on-chain events
- Real-time indexing as new blocks are produced

## Alpha Edge

- **Custom real-time indexing**: build analytics on ANY on-chain event that no commercial platform covers. If a new DeFi protocol launches and you want to track all liquidations, large swaps, or governance votes in real time, deploy a subgraph and you have a queryable API within hours
- **DEX analytics without intermediaries**: query every trade on Uniswap, SushiSwap, or any DEX directly -- track whale swaps, new token listings, and liquidity changes before analytics platforms surface them
- **Lending protocol monitoring**: track borrowing rates, utilization, liquidation thresholds, and large position changes on Aave/Compound in real time
- **Governance intelligence**: monitor DAO governance votes, proposal submissions, and delegate activity across protocols
- **Build what does not exist yet**: when a new narrative or protocol emerges in DeFi, The Graph lets you index and analyze it before [[nansen]] or [[arkham-intelligence]] add support

## Key Features

- **Subgraph Studio**: deploy, test, and manage custom subgraphs with a visual interface
- **GraphQL API**: query indexed blockchain data with standard GraphQL -- familiar to any web developer
- **Explorer**: browse and query thousands of existing community-deployed subgraphs
- **Multi-Chain**: supports Ethereum, Polygon, Arbitrum, Optimism, Avalanche, Celo, Gnosis, and more
- **Decentralized Network**: indexers, curators, and delegators maintain data availability via GRT staking
- **Real-Time Indexing**: subgraphs update as new blocks are confirmed on-chain

## Who Uses It

- DeFi protocols using The Graph as their backend data layer (Uniswap, Aave, Synthetix, and hundreds more)
- Analytics platforms building on top of subgraph data (many crypto dashboards query The Graph under the hood)
- Traders and researchers building custom analytics dashboards for specific protocols or strategies
- dApp developers who need on-chain data without running their own indexing infrastructure
- Data scientists pulling structured blockchain data for academic research or [[backtesting]]
- Anyone who needs to ask a specific question about on-chain activity that no existing platform answers

The Graph is infrastructure, not a finished analytics product. Use it when [[nansen]], [[glassnode]], or [[arkham-intelligence]] do not cover the specific on-chain data you need -- or when you want to build your own analytics without running full nodes.
