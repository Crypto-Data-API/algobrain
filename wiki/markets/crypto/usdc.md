---
title: "USD Coin (USDC)"
type: entity
created: 2026-04-07
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, regulation, stablecoins]
aliases: ["Circle USDC", "USD Coin", "USDC"]
entity_type: protocol
founded: 2018
headquarters: "Boston, USA (Circle)"
website: "https://www.circle.com"
related: ["[[aave]]", "[[base]]", "[[binance]]", "[[blackrock]]", "[[cctp]]", "[[centre-consortium]]", "[[circle]]", "[[coinbase]]", "[[crypto-markets]]", "[[dai]]", "[[defi]]", "[[ethereum]]", "[[regulation]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-attestations]]", "[[stablecoin-competition]]", "[[stablecoin-depegs]]", "[[stablecoin-regulation]]", "[[stablecoin-yield]]", "[[stablecoin-yields]]", "[[stablecoins]]", "[[usdt]]"]
---

USD Coin (USDC) is the **second-largest [[stablecoins|stablecoin]]** by market capitalisation and one of the largest crypto assets overall (rank #5), issued by [[circle|Circle Internet Financial]]. It is a US-dollar-pegged, fiat-collateralised stablecoin deployed natively across [[ethereum|Ethereum]], [[solana|Solana]], [[base|Base]] and 25+ other chains. USDC is widely regarded as the most transparent and regulatory-compliant major stablecoin, with 100% reserves backed by short-dated US Treasuries and cash deposits at regulated financial institutions.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | USDC |
| **Market Cap Rank** | #5 |
| **Market Cap** | $74.82B |
| **Current Price** | $0.9998 |
| **24h Volume** | $7.67B |
| **24h Change** | +0.001% |
| **7d Change** | +0.002% |
| **Circulating Supply** | 74.83B USDC |
| **Total Supply** | 74.83B USDC |
| **Max Supply** | Uncapped (supply = reserves; mint/burn on demand) |
| **All-Time High** | $1.043 (2018-11-15) |
| **All-Time Low** | $0.8776 (2023-03-11, SVB de-peg) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

As a fiat-backed [[stablecoin]], USDC is **designed to hold $1.00** — its near-zero 24h/7d change is the intended behaviour, not a tradable signal. The relevant "price" risk is **de-peg tail risk** (see the SVB section below), not directional volatility. USDC held its peg through the **extreme fear** macro backdrop (Crypto [[fear-and-greed-index|Fear & Greed Index]] = 23, long-horizon "Established Bear Market" regime as of 2026-06-20); in risk-off regimes USDC supply typically contracts as holders redeem to T-bills, while [[usdt|USDT]] tends to hold or grow on emerging-market demand. Note the market cap (~$74.8B) is well above the ~$30-35B level of early 2024, reflecting post-[[stablecoin-regulation|GENIUS/MiCA]] institutional adoption.

## Overview

USDC launched in September 2018 as a joint venture between Circle and [[coinbase|Coinbase]] under the Centre Consortium. The consortium set standards for fiat-backed stablecoins on public blockchains, with Circle as the sole issuer. In August 2023, Centre Consortium was dissolved and Circle assumed full governance and operational control of USDC.

Circle was founded in 2013 by Jeremy Allaire and Sean Neville, originally as a crypto payments company. The firm pivoted to focus primarily on USDC and stablecoin infrastructure, positioning itself as a financial infrastructure provider rather than a crypto company.

## Reserve Backing and Transparency

USDC reserves are held in two forms:

1. **Short-term US Treasury securities** -- managed through the Circle Reserve Fund, a registered government money market fund operated by BlackRock
2. **Cash deposits** at regulated US financial institutions

Circle publishes **monthly reserve attestation reports** conducted by Deloitte, a Big Four accounting firm. Each report confirms that the value of USDC reserves equals or exceeds the total USDC in circulation. This stands in stark contrast to [[usdt|Tether]], which publishes quarterly attestations by the smaller firm BDO Italia and has never undergone a full audit by a Big Four firm.

The reserve composition is intentionally conservative: short-duration US government obligations and cash, with no commercial paper, corporate bonds, or crypto assets in the reserve portfolio.

## Multi-Chain Deployment

USDC is natively issued on multiple blockchains:

| Blockchain | Notes |
|-----------|-------|
| [[ethereum|Ethereum]] | Largest USDC supply, primary DeFi chain |
| Solana | Second-largest deployment, fast/cheap transfers |
| Avalanche | Early multi-chain expansion |
| Polygon | L2 scaling for Ethereum |
| Arbitrum | [[layer-2]] rollup, growing DeFi ecosystem |
| Optimism | [[layer-2]] rollup |
| Base | Coinbase's L2, strong USDC integration |
| Stellar | Cross-border payments focus |
| NEAR | Newer deployment |

### Cross-Chain Transfer Protocol (CCTP)

Circle's CCTP enables **native USDC bridging** across supported blockchains. Unlike wrapped or bridged tokens (which introduce additional smart contract risk), CCTP burns USDC on the source chain and mints native USDC on the destination chain. This eliminates the need for third-party bridges and their associated security risks.

## Regulatory Positioning

Circle has pursued an aggressive regulatory compliance strategy, positioning USDC as the "institutional-grade" stablecoin:

- **United States**: Circle holds state money transmitter licences in 40+ US states. USDC is likely to be classified as a "payment stablecoin" under proposed federal legislation (GENIUS Act / CLARITY Act). See [[stablecoin-regulation]].
- **European Union**: Circle obtained an Electronic Money Institution (EMI) licence under [[stablecoin-regulation|MiCA]] (Markets in Crypto-Assets Regulation), making USDC one of the first MiCA-compliant stablecoins. As Tether has NOT obtained MiCA compliance, several EU exchanges delisted [[usdt|USDT]], shifting European markets toward USDC.
- **Other jurisdictions**: VASP registrations in multiple countries. Circle is registered in the UK and Singapore. See [[vasp-regulation]].

This compliance-first approach differentiates USDC from competitors and gives it a structural advantage as global stablecoin regulation tightens.

## Silicon Valley Bank Crisis (March 2023)

On March 10, 2023, Silicon Valley Bank (SVB) failed -- the second-largest US bank failure in history. Circle disclosed that approximately **$3.3 billion** of USDC's cash reserves (out of ~$40B total at the time) were held at SVB.

The market reaction was immediate and severe:

- USDC traded as low as **$0.87** on decentralised exchanges over the weekend
- [[dai|DAI]] also de-pegged to ~$0.89, since a significant portion of DAI's collateral was USDC
- Curve 3pool became heavily imbalanced as holders fled to [[usdt|USDT]]
- CEX prices lagged the de-peg, creating arbitrage between DEX and CEX

On Monday, March 13, the Federal Reserve and FDIC announced that **all SVB depositors would be made whole**, regardless of the $250,000 FDIC insurance limit. USDC's peg was restored within hours.

**Key lessons from the SVB de-peg:**
- Even "fully backed" stablecoins carry **banking counterparty risk**
- The DEX price is the "real-time" price during stress events -- CEX prices can lag
- Concentration of reserves at a single bank creates systemic vulnerability
- Government intervention (FDIC backstop) was ultimately what restored the peg
- USDC diversified its banking relationships after this event

See [[stablecoin-depegs]] for a comprehensive history of de-peg events.

## Key Partnerships

| Partner | Relationship |
|---------|-------------|
| [[coinbase|Coinbase]] | Co-created USDC. Revenue-sharing agreement on USDC interest income. Coinbase promotes USDC on its platform and offers USDC rewards to users |
| BlackRock | Manages the Circle Reserve Fund (USDC's reserve portfolio) |
| Visa | USDC settlement pilot -- Visa settles some transactions using USDC on Ethereum and Solana |
| Mastercard | Partnership for crypto-to-fiat settlement |
| Stripe | Crypto payouts in USDC for platform merchants |

## Revenue Model

Circle earns revenue from the **yield on USDC reserves**. With US Treasuries yielding 4-5% in 2023-2024, Circle generated over **$1.5 billion in revenue** in 2023 from interest on reserves alone.

Critically, USDC holders do **NOT** receive any of this yield. When a user holds $10,000 in USDC, Circle earns ~$450/year in Treasury yield on the backing reserves while the holder earns nothing. This is the core business model -- it is essentially a money market fund where the depositors receive no interest. Some newer stablecoins (sDAI, USDY, sFRAX) are challenging this model by passing yield through to holders. See [[stablecoin-yields]].

Circle shares a portion of USDC interest revenue with [[coinbase|Coinbase]] under their partnership agreement. Coinbase reported earning $468M from USDC-related revenue in 2023.

## USDC vs USDT

| Dimension | USDC | [[usdt|USDT]] |
|-----------|------|------|
| Market cap | ~$74.8B (rank #5, 2026-06-20) | larger (rank #3; see [[usdt]]) |
| Transparency | Monthly Big Four attestation (Deloitte) | Quarterly attestation (BDO Italia) |
| Regulatory status | Money transmitter licences, MiCA-compliant | No major regulatory licence, BVI-based |
| Primary chains | Ethereum, Solana, Base | Tron, Ethereum |
| DeFi usage | Preferred for composability, institutional DeFi | Dominant in CEX trading pairs |
| Geographic focus | US, Europe, institutional | Asia, emerging markets, retail |
| Reserve composition | 100% Treasuries + cash | ~85% Treasuries + Bitcoin + gold + loans |
| Freezing capability | Yes (OFAC compliance) | Yes (law enforcement requests) |

In [[defi|DeFi]], USDC is often the preferred stablecoin due to its transparency and regulatory positioning. It is a major trading pair on [[uniswap|Uniswap]], a core lending asset on [[aave|Aave]], and a base pair on centralised exchanges. However, [[usdt|USDT]] has deeper overall liquidity, lower slippage on most trading pairs, and dominant market share in Asia.

## Use in DeFi

USDC is deeply integrated into the [[defi|DeFi]] ecosystem:

- **Lending**: Core supply/borrow asset on [[aave|Aave]], Compound, and Morpho. See [[defi-lending]]
- **AMM liquidity**: Major pair in [[automated-market-maker|AMM]] pools (USDC/ETH, USDC/USDT). Stable pairs have minimal [[impermanent-loss]]
- **Yield strategies**: Base asset for numerous yield farming strategies. See [[stablecoin-yields]]
- **Derivatives**: Margin asset on decentralised perpetual exchanges
- **Cross-chain DeFi**: CCTP enables native USDC movement across chains without bridge risk

## Circle's IPO Plans

Circle filed an S-1 registration statement with the [[sec|SEC]] in January 2024 for a public listing on the New York Stock Exchange. A previous attempt via SPAC merger in 2022 fell through due to market conditions. If successful, Circle would be one of the first major stablecoin issuers to become a publicly traded company, further increasing transparency through SEC reporting requirements.

## Stablecoin Peer Comparison

| Stablecoin | Type | Issuer | Backing | Reg. status |
|---|---|---|---|---|
| **USDC** | Fiat-backed | [[circle|Circle]] | 100% Treasuries + cash | MiCA EMI, US money-transmitter licences |
| [[usdt|USDT]] | Fiat-backed | Tether | Treasuries + BTC/gold/loans | BVI-based, no MiCA |
| [[dai|DAI]] | Crypto-collateralised | MakerDAO | Crypto + RWA (incl. USDC) | Decentralised |
| First Digital / FDUSD | Fiat-backed | First Digital | Cash + T-bills | Hong Kong |
| USDe (Ethena) | Synthetic / delta-neutral | Ethena | Staked ETH + perp shorts | Unregulated |

USDC's differentiation is **regulatory clarity and transparency**, not size — it trades a portion of [[usdt|USDT]]'s liquidity/yield for auditability and institutional acceptability. See [[stablecoin-competition]].

---

## Risks

- **Banking counterparty risk** — the 2023 SVB event proved even "fully backed" USDC can de-peg if a reserve bank fails. Circle has since diversified custodians, but cash deposits are not FDIC-insured beyond $250k limits.
- **Regulatory / freezing risk** — USDC is centrally controlled; Circle can and does **freeze addresses** for OFAC/law-enforcement compliance. This is a feature for institutions and a risk for permissionless DeFi users.
- **Issuer concentration** — a single issuer (Circle) is a single point of failure (governance, banking, smart-contract upgrade keys).
- **Yield asymmetry** — holders earn nothing while Circle keeps the Treasury yield; competing yield-bearing stablecoins (sDAI, USDY, USDe) and tokenised T-bills erode USDC's idle-balance appeal. See [[stablecoin-yields]].
- **Smart-contract / bridge risk** — mitigated by CCTP for native transfers, but third-party-bridged USDC variants still carry wrapper risk.
- **Depeg contagion** — because [[dai|DAI]] and other protocols hold USDC as collateral, a USDC de-peg propagates across DeFi. See [[stablecoin-depegs]].

---

## Related

- [[stablecoins]] -- Overview of stablecoin types and market
- [[usdt]] -- Tether, the largest stablecoin competitor
- [[dai]] -- Decentralised alternative
- [[circle]] -- Circle Internet Financial (USDC issuer)
- [[coinbase]] -- Key partner and distribution channel
- [[defi]] -- Ecosystem where USDC is widely used
- [[aave]] -- Major DeFi lending protocol using USDC
- [[stablecoin-regulation]] -- Regulatory landscape
- [[stablecoin-depegs]] -- History of de-peg events including USDC/SVB
- [[stablecoin-yields]] -- Earning yield on USDC
- [[ethereum]] -- Primary deployment chain

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 74.83B USDC |
| **Total Supply** | 74.83B USDC |
| **Max Supply** | Uncapped — supply is fully reserve-backed and elastic |
| **Fully Diluted Valuation** | ~$74.8B (= market cap) |
| **Market Cap / FDV Ratio** | ~1.00 |

USDC has **no dilution overhead in the usual token sense**: it is not an emissions-driven asset. Every USDC is minted only when $1 of reserves is deposited and burned on redemption, so circulating ≈ total supply and **MC/FDV ≈ 1.00**. "Supply growth" reflects net new dollar deposits, not inflation — it is a demand signal, not dilution. This is the structural opposite of governance tokens like [[pendle]] or [[kamino]] that carry large uncirculated allotments. Categories include USD Stablecoin, MiCA-Compliant Stablecoin, Fiat-backed Stablecoin, Made in USA, plus 30+ chain-ecosystem tags ([[ethereum|Ethereum]], [[solana|Solana]], [[base|Base]], Avalanche, [[arbitrum|Arbitrum]], Polygon, Tron, Stellar, and more).

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.043 (2018-11-15) |
| **All-Time Low** | $0.8776 (2023-03-11, SVB de-peg) |
| **24h Change** | +0.001% |
| **7d Change** | +0.002% |

> Price-change figures reconciled to the 2026-06-20 snapshot. For a fiat-backed stablecoin these are intentionally ~0; the meaningful history is the de-peg record (see SVB section). Stale 30d/1y rows removed.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` |
| Monad | `0x754704bc059f8c67012fed69bc8a327a5aafb603` |
| Moonriver | `0xffffffff7d2b0b761af01ca8e25242976ac0ad7d` |
| Sui | `0xdba34672e30cb065b1f93e3ab55318768fd6fef66c15942c9f7cb846e2f900e7::usdc::USDC` |
| Polkadot | `1337` |
| Xrp | `5553444300000000000000000000000000000000.rGm7WCVp9gb4jZHWTEtGUr4dd74z2XuWhE` |
| Sonic | `0x29219dd400f2bf60e5a23d13be72b486d4038894` |
| Zksync | `0x1d17cbcf0d6d143135ae902365d2e5e2a16538d4` |
| Hedera Hashgraph | `0.0.456858` |
| Ink | `0x2d270e6886d130d724215a266106e6832161eaed` |
| Unichain | `0x078d782b760474a361dda0af3839290b0ef57ad6` |
| Xdc Network | `0xfa2958cb79b0491cc627c1557f441ef849ca8eb1` |
| Hyperevm | `0xb88339cb7199b77e23db6e890353e22632ba630f` |
| Plume Network | `0x222365ef19f7947e5484218551b56bb3965aa7af` |
| Sei V2 | `0xe15fc38f6d8c56af07bbcbe3baf5708a2bf42392` |
| Near Protocol | `17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1` |
| Base | `0x833589fcd6edb6e08f4c7c32d4f71b54bda02913` |
| Algorand | `31566704` |
| Tron | `TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8` |
| Celo | `0xceba9300f2b948710d2653dd7b07f33a8b32118c` |
| Morph L2 | `0xcfb1186f4e93d60e60a8bdd997427d1f33bc372b` |
| Stellar | `CCW67TSZV3SSS2HXMBQ5JFGCKJNXKZM7UQUWUZPUTHXSTZLEO7SJMI75` |
| World Chain | `0x79a02482a880bce3f13e09da970dc34db4cd24d1` |
| Polygon Pos | `0x3c499c542cef5e3811e1192ce70d8cc03d5c3359` |
| Arbitrum One | `0xaf88d065e77c8cc2239327c5edb3a432268e5831` |
| Solana | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Starknet | `0x33068f6539f8e6e6b131e6b2b814e6c34a5224bc66947c47dab9dfee93b35fb` |
| Optimistic Ethereum | `0x0b2c639c533813f4aa9d7837caf62653d097ff85` |
| Aptos | `0xbae207659db88bea0cbead6da0ed00aac12edcdda169e591cd41c94180b46f3b` |
| Avalanche | `0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | USDC/USDT | N/A |
| Kraken | USDC/EUR | N/A |
| Bitget | USDC/USDT | N/A |
| KuCoin | ETH/USDC | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.circle.com/en/usdc](https://www.circle.com/en/usdc) |
| **Discord** | [https://discord.com/invite/buildoncircle](https://discord.com/invite/buildoncircle) |
| **GitHub** | [https://github.com/centrehq/centre-tokens](https://github.com/centrehq/centre-tokens) |
| **Whitepaper** | [https://www.circle.com/legal/mica-usdc-whitepaper](https://www.circle.com/legal/mica-usdc-whitepaper) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 733 |
| **GitHub Forks** | 529 |
| **Commits (4 weeks)** | 1 |
| **Pull Requests Merged** | 273 |
| **Contributors** | 29 |

---

## Market Structure & Liquidity

USDC is one of the deepest-liquidity assets in all of crypto. It functions as a **base trading pair and settlement layer** rather than a directional trade:

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.67B |
| **Market Cap Rank** | #5 |
| **Volume / Market Cap** | ~10% daily turnover |
| **Role** | Quote currency / margin collateral / DeFi base asset |
| **Last Updated** | 2026-06-20 |

- **Spot venues:** quoted on every major CEX ([[binance|Binance]], [[coinbase|Coinbase]], Kraken, Bitget, KuCoin) and as a core stable pair on DEXes ([[uniswap|Uniswap]], [[curve-finance|Curve]] 3pool/stable pools, Solana DEXes via [[kamino]]/Orca/Raydium).
- **Derivatives & perps:** USDC is a primary **margin collateral** on derivatives venues — notably [[hyperliquid|Hyperliquid]], where USDC is the settlement asset for [[perpetual-futures|perpetual futures]]. It is also widely used as collateral on dYdX, GMX and CEX perp markets. USDC itself is not a directional perp; rather it underpins others.
- **Cross-chain liquidity:** CCTP (below) lets USDC move natively across 25+ chains without bridge-wrapping risk, concentrating liquidity rather than fragmenting it.
- **De-peg arbitrage:** during stress, the DEX price (e.g. Curve 3pool) leads the CEX price; arbitrageurs who can mint/redeem 1:1 with Circle backstop the peg.

---

## Trading Profile

### Venues & liquidity

USDC is a USD-pegged stablecoin traded on [[binance|Binance]] (and every other major CEX/DEX). It is a **peg / cash-management instrument, NOT a directional asset** — the trade is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. On Binance USDC is a quote and settlement asset (USDC/USDT and fiat pairs) rather than a leveraged directional market, so "leverage" applies to the *strategies built on top of it* (carry, delta-neutral yield) rather than to USDC itself. Because it is one of the deepest-liquidity assets in crypto and available natively across 25+ chains via CCTP, execution slippage is minimal and sizing is rarely liquidity-constrained; the practical constraint is redemption/mint access (1:1 with Circle) and cross-venue price dislocation during stress, which is where arbitrage capacity — not book depth — sets the effective size.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — buy USDC below $1.00 during banking/stress events (e.g. the 2023 SVB dislocation to ~$0.87) and hold to par as reserves are backstopped.
- [[stablecoin-pair-arbitrage]] — exploit USDC/USDT and USDC/DAI spreads across CEX and Curve stable pools when one leg drifts off peg.
- [[mint-parity-arbitrage]] — arb the secondary-market price against Circle's 1:1 mint/redeem, the mechanism that ultimately re-anchors the USDC peg.
- [[stablecoin-yield]] — deploy idle USDC into lending (Aave/Compound/Morpho) or tokenised-T-bill wrappers to earn the yield USDC itself does not pass through to holders.
- [[delta-neutral-yield-farming]] — use USDC as the stable base leg in market-neutral LP/farming structures where directional exposure is hedged out.
- [[carry-trade]] — fund positions in USDC to harvest rate differentials while treating the peg as (near-)fixed collateral.

### Volatility & regime character

Peg is normally extremely tight (24h range roughly $0.9997–$1.00), so realised volatility is near-zero by design and the meaningful history is the **depeg record**, not price trend. Backing model: 100% fiat-collateralised (short-dated US Treasuries via the BlackRock-managed Circle Reserve Fund plus cash at regulated banks), with elastic mint/burn keeping supply ≈ reserves. Redemption mechanics (1:1 with Circle) are the anchoring force: in calm regimes the peg is boringly stable; in banking/liquidity stress the DEX price (e.g. Curve 3pool) leads and can gap down before mint/redeem arbitrage restores par. The notable historical episode is the March 2023 SVB event, when USDC traded as low as ~$0.87 before recovering within hours after the FDIC backstop.

### Risk flags

- **Depeg / banking counterparty risk** — even a "fully backed" stablecoin can break peg if a reserve bank fails; cash deposits are not FDIC-insured beyond standard limits.
- **Reserve / backing transparency** — dependent on monthly attestations rather than a continuous audit; reserve concentration at any single custodian is a tail risk.
- **Redemption gating** — 1:1 redemption runs through Circle and its banking rails, which can slow or gate during stress, widening the arb needed to hold the peg.
- **Regulatory / freezing** — USDC is centrally controlled and Circle can freeze addresses for OFAC/law-enforcement compliance; regulatory shifts (GENIUS/MiCA) can reshape access and eligibility.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=USDCUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=USDCUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=USDCUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=USDCUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDC |
| **Market Cap Rank** | #5 |
| **Market Cap** | $73.09B |
| **Current Price** | $0.9999 |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed Stablecoin, Made in USA, Base Native, MiCA-Compliant Stablecoin, GENIUS Act Compliant Stablecoin |
| **Website** | [https://www.circle.com/en/usdc](https://www.circle.com/en/usdc) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 73.09B USDC |
| **Total Supply** | 73.10B USDC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $73.09B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $11.97B |
| **Market Cap Rank** | #5 |
| **24h Range** | $0.9997 — $1.00 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---
