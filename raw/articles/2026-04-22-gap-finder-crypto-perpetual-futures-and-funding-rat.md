<!-- Gap finder: crypto perpetual futures and funding rate trading strategies -->
<!-- Date: 2026-04-22 -->

You are missing critical gaps in **decentralized perpetuals (Perp DEXs)**, **regulatory frameworks (CFTC)**, **specific high-volume exchanges (Binance, Bybit)**, and **2024–2026 market shifts** like the explosion of onchain derivatives. Below are the top 25 most impactful missing items, prioritized by trading relevance.

---

### 1. **Key Entities Missing** (Companies, Protocols, Exchanges)

| Name | One-Line Description | Why It Matters for Traders |
|------|---------------------|----------------------------|
| **Binance** | World’s largest crypto derivatives exchange by volume, offering perps, futures, options. | Dominates liquidity; funding rates and leverage here set market benchmarks[7][8]. |
| **Bybit** | Top-tier perp exchange with deep liquidity, up to 100x leverage, and strong Asia presence. | Critical for high-frequency funding rate arbitrage; often has tighter spreads than OKX[7]. |
| **dYdX** | Leading decentralized perp DEX on StarkNet, offering self-custodial leveraged trading. | Represents the fastest-growing Perp DEX segment; $2.1T volume in 2025[3]. |
| **GMX** | Perp DEX on Arbitrum with v2 architecture, enabling capital-efficient leverage. | Key player in onchain derivatives; integrates with MetaMask Perps for wallet access[3]. |
| **MetaMask Perps** | Self-custodial wallet integration connecting users to onchain perp DEXs. | Enables non-custodial perp trading; bridges Web3 wallets to $6.7T perp DEX volume[3]. |
| **CFTC (Commodity Futures Trading Commission)** | U.S. regulator petitioning to exempt digital perps from swap rules (Feb 2026). | Regulatory clarity will reshape perp DEX compliance and institutional adoption[5]. |
| **Bitget** | Top-5 global perp exchange by volume, offering 125x leverage and USDT/USDC pairs. | High-leverage venue for altcoin perps; growing liquidity in emerging markets[9]. |
| **Phemex** | Exchange with 500+ perps, 100x leverage, and pre-market perp trading before spot listing. | Unique for early altcoin exposure; 100% Proof of Reserves adds trust[2]. |
| **Neutrl Protocol** | Issuer of NUSD (market-neutral synthetic dollar) backed by delta-neutral trading. | Provides stable, non-fiat collateral for perp strategies; avoids fiat stablecoin risk[8]. |
| **Hyperliquid** | High-performance L1 for perp DEXs, hosting Alfred’s systematic basket library. | Core infrastructure for institutional perp strategies; supports HLP vault architecture[9]. |

---

### 2. **Important Concepts/Strategies Missing**

| Name | One-Line Description | Relevance to Trading |
|------|---------------------|----------------------|
| **Funding Rate Arbitrage** | Profiting from persistent differences in perp funding rates across exchanges. | Core strategy for carry traders; exploits rate divergence between Binance/Bybit/OKX. |
| **Perp DEX Liquidity Provision** | Providing capital to onchain perp pools (e.g., dYdX, GMX) to earn fees. | High-yield alternative to CeFi; exposed to smart contract and oracle risk. |
| **Mark Price Liquidation** | Liquidation triggered by mark price (not last price) to prevent manipulation. | Critical risk parameter; affects leverage safety on Bybit/Binance vs. older venues. |
| **Cross vs. Isolated Margin** | Margin modes: cross uses full balance, isolated limits risk per position. | Determines capital efficiency and blow-up risk in high-leverage perp trading. |
| **Pre-Market Perp Trading** | Trading perps on tokens before spot listing (e.g., Phemex). | Early alpha for altcoins; avoids spot listing volatility. |
| **Onchain Oracle Manipulation Risk** | Perp DEXs rely on oracles; manipulation can trigger false liquidations. | Unique risk in DeFi perps; affects strategy design for GMX/dYdX. |
| **Regulatory Arbitrage (CeFi vs. DeFi)** | Trading perps on offshore CeFi vs. self-custodial DEXs to avoid compliance. | Institutional traders use DEXs to bypass CFTC/SEC constraints[5]. |
| **Delta-Neutral Perp Hedging** | Using perps to hedge spot exposure while earning funding. | Core for market-neutral strategies; pairs with NUSD synthetic dollar[8]. |
| **Volatility-Adjusted Position Sizing** | Scaling perp positions based on intraday vol (e.g., crypto perp backtest pitfalls). | Prevents over-leverage during flash crashes; critical for 24/7 markets[3]. |
| **Funding Harvesting Vaults** | Automated strategies (e.g., Hyperliquid HLP) that collect perp funding payments. | Passive yield source; structurally distinct from liquidation/market-making[4]. |

---

### 3. **Data Sources/Tools Missing**

| Name | Description | Why Traders Use It |
|------|-------------|--------------------|
| **CoinGecko Perp DEX Report** | Annual report tracking perp DEX volume (e.g., $6.7T in 2025). | Benchmark for DEX market share growth; tracks 5x expansion since 2024[3]. |
| **CoinMarketCap Derivatives Rankings** | Real-time rankings of CeFi perp exchanges by volume (Binance #1). | Identifies liquidity leaders for funding rate arbitrage[7]. |
| **LiquidityFinder Crypto Derivatives** | Analysis of top 12 perp exchanges, including Bitget, Bybit, OKX. | Compares fees, leverage, and liquidity across venues[9]. |
| **MetaMask Perps Dashboard** | In-wallet interface showing perp DEX positions and rates. | Enables self-custodial perp trading; integrates with dYdX/GMX[3]. |
| **CFTC Innovation Blockchain Petition** | Official document on exempting digital perps from swap rules. | Regulatory roadmap for institutional perp DEX adoption[5]. |
| **CryptoFuturesPlatform.com** | Updated 2026 guide to top 7 perp platforms (Binance, Bybit, etc.). | Beginner/intermediate guide to fees, leverage, and risks[8]. |

---

### 4. **Recent Developments (2024–2026)**

| Development | Description | Trading Impact |
|-------------|-------------|----------------|
| **Perp DEX Volume Explosion** | $6.7T cumulative volume in 2025 (346% increase from 2024); DEX share hit 10.2%[3]. | Shifts liquidity from CeFi; enables self-custodial strategies. |
| **CFTC Exemption Petition (Feb 2026)** | Petition to exempt digital perps from swap rules, treating them as futures[5]. | Could legitimize perp DEXs for institutions; reduces regulatory risk. |
| **Perp DEXs on Non-Crypto Assets** | Platforms now offer perps on gold, silver, FX, and tokenized equities[3]. | Diversifies perp strategies beyond crypto; new arbitrage opportunities. |
| **MetaMask Perps Integration** | Wallet now connects directly to onchain perp DEXs without CeFi accounts[3]. | Democratizes perp access; reduces counterparty risk. |
| **Phemex Pre-Market Perps** | Trading perps before spot listing; 500+ perps with 100x leverage[2]. | Early alpha for altcoins; avoids spot listing volatility. |
| **Hyperliquid L1 for Perps** | High-performance chain hosting Alfred’s systematic basket library[9]. | Enables institutional-grade perp strategies with low latency. |
| **Mark Price Standardization** | CeFi exchanges (Binance, Bybit) now use mark price for liquidation[2]. | Reduces manipulation risk; affects leverage safety. |
| **100% Proof of Reserves (Phemex)** | Cryptographically verifiable reserves, not just claimed[2]. | Adds trust for high-leverage perp trading; reduces counterparty risk. |
| **Cross-Margin Perp Adoption** | CeFi exchanges now support cross-margin for perps (Binance, Bybit)[2]. | Improves capital efficiency; reduces blow-up risk. |
| **Regulatory Arbitrage Surge** | Institutions shift to perp DEXs to bypass CFTC/SEC constraints[5]. | Changes liquidity dynamics; increases DEX volume share. |

---

### Summary of Top 5 Gaps to Address First
1. **Perp DEXs (dYdX, GMX, MetaMask Perps)** – Fastest-growing segment; $6.7T volume.
2. **Binance & Bybit** – Dominant CeFi venues; set funding rate benchmarks.
3. **CFTC Exemption Petition** – Regulatory clarity will reshape perp DEX adoption.
4. **Funding Rate Arbitrage** – Core strategy for carry traders; exploits CeFi/DeFi divergence.
5. **Onchain Oracle Risk** – Unique perp DEX risk; affects strategy design.

These gaps are essential for a complete, trading-relevant wiki on crypto perpetual futures and funding rate strategies.

---

## Citations

1. https://cryptoslate.com/crypto-exchanges/futures/
2. https://phemex.com/blogs/top-crypto-exchanges-in-2026
3. https://metamask.io/news/bitcoin-futures-trading-in-2026
4. https://www.youtube.com/watch?v=lWziwiy4acg
5. https://www.cftc.gov/media/13716/innovation_BlockchainAssn02242026/download
6. https://bitcoinfoundation.org/news/opinion/best-crypto-exchanges/
7. https://coinmarketcap.com/rankings/exchanges/derivatives/
8. https://cryptofuturesplatform.com
9. https://liquidityfinder.com/insight/crypto/the12-best-crypto-derivatives-exchanges
