---
title: "Bedrock"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["BR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bedrockdao.com/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[liquid-staking]]", "[[restaking]]"]
---

# Bedrock

**Bedrock** (ticker **BR**) is the governance token of **Bedrock**, a multi-asset **liquid-restaking** protocol. Bedrock issues liquid (re)staking tokens — such as uniETH for [[ethereum]] and uniBTC for [[bitcoin]] — that let users earn staking and [[restaking]] rewards while keeping their assets liquid and usable in DeFi. The **BR** token governs the protocol via a vote-escrow (veBR) model. It is a small-cap DeFi governance asset, ranked **#582** by market capitalization.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | BR |
| **Current Price** | $0.138931 |
| **Market Cap** | $34.91M |
| **Market Cap Rank** | #582 |
| **24h Volume** | $5.88M |
| **24h Change** | -2.04% |
| **7d Change** | +15.28% |
| **Fully Diluted Valuation** | $138.93M |
| **All-Time High** | $0.257114 (2026-04-15) — −46.0% |
| **All-Time Low** | $0.039208 (2025-04-18) |

Trading backdrop: the broad crypto market sits in **extreme fear** ([[fear-and-greed-index|Crypto Fear & Greed Index]] = 23) amid an **"Established Bear Market"** as of 2026-06-21. BR is down ~46% from its April 2026 high but has **rallied ~+15% over the past week** (bucking the fearful tape) even as it slipped ~2% on the day; notably its 24h dollar volume (~$5.9M) is large relative to its $34.9M circulating market cap (~17% turnover), reflecting active speculative trading despite the small float.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 251.25M BR |
| **Total Supply** | 1.00B BR |
| **Max Supply** | 1.00B BR |
| **Market Cap** | $34.91M |
| **Fully Diluted Valuation** | $138.93M |
| **MC / FDV Ratio** | ~0.25 |

The **MC/FDV ratio of ~0.25** is the dominant tokenomics fact: only ~25% of the fixed 1B BR supply circulates, leaving ~750M BR (an FDV of ~$139M vs ~$35M circulating cap) still to unlock. This is a large dilution overhang typical of recently-launched DeFi governance tokens — every weekly/cliff unlock adds structural sell pressure that the small ~$35M float must absorb.

**Governance model:** BR is locked 1:1 into **veBR** (vote-escrowed BR); longer locks grant more voting power. veBR holders vote on protocol parameters, incentive structures, and **gauge allocations** that direct emissions across liquidity pools — a Curve-style ve-tokenomics design.

---

## How & Where It Trades

**Spot venues.** BR trades mainly as **BR/USDT** on Bitget and [[kucoin]], and on-chain across its multiple deployments. As a sub-$50M cap with a small float, liquidity is concentrated; the relatively high turnover suggests most volume is speculative rather than utility-driven.

**Liquid-restaking mechanics (the actual product).** Bedrock is a **liquid-restaking-token (LRT) issuer**, part of the [[restaking]] wave:

- **uniETH** — Bedrock's liquid staking/restaking token for [[ethereum]]; users deposit ETH, receive uniETH, and earn ETH staking plus restaking rewards while uniETH stays liquid for DeFi.
- **uniBTC** — Bedrock's BTCfi liquid-staking token, extending the model to [[bitcoin]] (CoinGecko tags BR as a BTCfi Protocol).
- **veBR gauge voting** — veBR holders steer BR emissions toward pools, aligning governance with where liquidity is most needed.
- **Multi-chain** — deployed on [[bnb]] Chain (native), Base, [[ethereum]], and Berachain, so its LRTs and governance span several ecosystems.

**Derivatives.** BR has no material perpetual-futures / [[hyperliquid]] listing; no meaningful funding-rate or open-interest data is available. Treat it as a spot-only small-cap.

---

## Use Case, Narrative & Category

Bedrock sits in the **liquid (re)staking + DeFi governance** category (CoinGecko tags: DeFi, Liquid Staking Governance Tokens, BTCfi Protocol, BNB/Base/Berachain/Ethereum ecosystems, Binance Wallet IDO). Its narrative rides two big themes — Ethereum **restaking** and **BTCfi** — by issuing liquid tokens that keep staked capital productive. Value accrues to BR/veBR through protocol fees and control over emissions, contingent on Bedrock's restaking TVL.

---

## Valuation Framing (qualitative)

- **TVL-multiple lens.** As a [[restaking|LRT]] governance token, BR should be read against restaking/BTCfi TVL and fee capture, not cash flows. Its ~$35M circulating cap is a function of TVL multiple plus a thin-float speculative premium.
- **Dilution caveat.** The ~0.25 MC/FDV means any "cheap" circulating-cap read is offset by ~750M BR of pending unlocks (FDV ~$139M, ~4× the float). On a fully-diluted basis BR is far less cheap than headline cap suggests.
- **BTCfi optionality.** uniBTC gives BR exposure to the emerging **BTCfi** theme — a differentiator vs pure-ETH LRTs; if BTC restaking scales, that is the upside lever.
- **Regime / float dynamics.** With [[fear-and-greed-index|Fear & Greed]] at 23, the LRT category is de-rated; BR's +15% week shows the small float cuts both ways — sharp rallies and sharp drawdowns on modest flow.

---

## Peer Comparison

| Protocol | Token | Category | Approx. cap | Differentiator |
|---|---|---|---|---|
| **Bedrock** | BR / veBR | Multi-asset LRT + BTCfi | ~$35M | uniETH + **uniBTC** (BTCfi); ve-gauge governance; multi-chain |
| [[puffer-finance\|Puffer]] | PUFFER / pufETH | ETH restaking | Outside top-1000 | Anti-slashing, decentralization-first |
| [[etherfi\|EtherFi]] | ETHFI / eETH | ETH restaking (largest) | Multi-$B | TVL scale, consumer products |
| [[renzo\|Renzo]] | REZ / ezETH | Multi-chain restaking | Mid-cap | Aggressive cross-chain distribution |

BR is a **small-cap, multi-asset** entrant whose distinctive angle is extending the liquid-restaking model to **BTC (uniBTC / BTCfi)** alongside ETH, plus Curve-style ve-gauge governance.

---

## Notable History

- Launched its BR governance token via a **Binance Wallet IDO** (CoinGecko tag), giving it early Binance-ecosystem distribution.
- All-time low of **$0.0392 on 2025-04-18** shortly after launch.
- ATH of **$0.257 on 2026-04-15**, since retraced ~46%.
- **~+15% week** into 2026-06-21 despite the extreme-fear backdrop; BR remains a high-dilution early-stage token with active speculative turnover.

---

## Risks

- **Heavy dilution** — only ~25% of supply circulates; ~750M BR of unlocks (FDV ~4x market cap) overhang the price.
- **Restaking systemic risk** — LRTs inherit slashing, re-hypothecation, and cascading-failure risks of the underlying restaking layers.
- **Small-cap volatility** — sub-$50M cap with high turnover; sharp drawdowns (e.g. -3.5% in 24h) are routine.
- **Multi-chain / smart-contract risk** — deployments across BNB, Base, Ethereum, and Berachain multiply the contract attack surface.
- **Bear-market regime** — extreme-fear ([[fear-and-greed-index|Fear & Greed]] = 23), established-bear-market backdrop pressures speculative DeFi governance tokens hardest.

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[ethereum]] · [[bitcoin]]
- [[restaking]]
- [[liquid-staking]]
- [[decentralized-finance]]
- [[puffer-finance]] · [[etherfi]] · [[renzo]] — peer LRT protocols
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000): price $0.138931, cap ~$34.91M, rank #582, ATH $0.257114 (2026-04-15), ATL $0.039208 (2025-04-18).
- General market knowledge; no specific wiki source ingested yet.

