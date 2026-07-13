---
title: "TokenPocket Token"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, defi, cross-chain]
aliases: ["TPT", "TokenPocket"]
entity_type: protocol
headquarters: "Hong Kong"
website: "https://tp.xyz/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[wallet]]"]
---

# TokenPocket Token

**TokenPocket Token** (TPT) is the utility token of **TokenPocket**, one of the longest-running multi-chain self-custody crypto [[wallet|wallets]]. Founded in April 2018 and headquartered in Hong Kong, TokenPocket provides a non-custodial wallet supporting a very large number of public chains, an in-app [[decentralized-exchange|DEX]] aggregator/swap, a dApp browser, and stablecoin payment features. TPT functions as the in-app utility and membership token across that ecosystem. It ranks **#848** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot, TPT traded at **$0.00585422** with a market cap of **$19,045,170** (rank **#848**), down **3.20%** over 24 hours and **9.18%** over 7 days — among the weaker performers in this cohort, consistent with a risk-off tape (Bitcoin near $64,508, Fear & Greed 21 / "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TPT |
| **Market Cap Rank** | #848 |
| **Market Cap** | $19,045,170 |
| **Current Price** | $0.00585422 |
| **24h Change** | -3.20% |
| **7d Change** | -9.18% |
| **Categories** | Wallet, BNB Chain Ecosystem, DeFi |
| **Website** | [https://tp.xyz/](https://tp.xyz/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## What TokenPocket does

TokenPocket is a **multi-chain, self-custody [[wallet]]** — the user holds their own private keys, and the app provides the interface to send, receive, swap, and interact with decentralized applications across dozens of blockchains. Its main product surfaces are:

- **Self-custody wallet** — key management across a wide range of EVM and non-EVM chains, with hardware-wallet and multi-sig support.
- **dApp browser** — an in-app gateway to [[decentralized-exchange|DeFi]] protocols, NFT marketplaces, and other dApps.
- **Swap / DEX aggregation** — built-in token swapping that routes through on-chain liquidity, including [[cross-chain]] swaps.
- **Stablecoin payments** — the project markets a stablecoin wallet/payment business covering many countries, claiming tens of millions of cumulative users and several million monthly actives (figures are project-stated; treat as marketing rather than verified metrics).

The wallet is widely used in Asian markets and the TRON/BNB Chain ecosystems in particular.

### Architecture — How the wallet works

A self-custody wallet like TokenPocket is, at its core, a **key-management and transaction-construction client**; it never holds user funds. The pieces:

**1. Key custody on-device.** The wallet generates a [[seed-phrase|BIP-39 seed phrase]] and derives per-chain private keys ([[hierarchical-deterministic-wallet|HD derivation]]) that are stored encrypted on the user's device. The app signs transactions locally and broadcasts them; nothing custodial sits server-side, which is the entire security premise (and risk surface — see below). It supports **hardware-wallet** signing (cold keys) and **multi-sig** for higher-assurance setups.

**2. Multi-chain RPC layer.** TokenPocket connects to RPC endpoints across dozens of EVM and non-EVM chains (Ethereum, BNB Chain, TRON, and many more), letting one app manage assets and dApps on all of them. Chain coverage breadth is its headline feature.

**3. dApp browser + WalletConnect.** An in-app browser injects a Web3 provider so the wallet can connect to DeFi, NFT, and other dApps directly, plus [[walletconnect|WalletConnect]] for external sites — the wallet becomes the signing layer for the broader on-chain app ecosystem.

**4. In-app swap / aggregation.** Built-in swaps route orders through on-chain liquidity (and [[cross-chain]] routes), so a user can trade without leaving the app. This is also a **monetization surface** — swap routing can earn fees/spread — which matters because wallets are otherwise hard to monetize.

**5. Stablecoin payments rail.** A separate marketed business layers stablecoin send/receive/payment features on top of the wallet across many countries (project-stated metrics; treat as marketing).

## Token role

TPT is the **utility and membership token** of the TP ecosystem. Its stated functions are as an in-app payment/benefits asset and a "membership" credential unlocking premium features, with applications described as expanding over time. The economic story centers on **deflation**: TPT is positioned as fully circulating with a long-term burn model. Per the project, starting 2025-07-01 the TokenPocket Foundation began a biannual **buyback-and-burn** program intended to shrink total supply from ~3.466 billion toward 1 billion tokens. If executed, this is the primary token-demand sink, since TPT — like most wallet tokens — does not secure a chain and the wallet itself functions without it.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.25B TPT |
| **Total Supply** | 3.25B TPT |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $21.62M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1456 (2021-05-14) |
| **Current vs ATH** | -95.44% |
| **All-Time Low** | $0.00012901 (2020-03-27) |
| **Current vs ATL** | +5047.36% |
| **24h Change** | -3.20% |
| **7d Change** | -9.18% |
| **1y Change** | -7.64% |

> *24h/7d figures are the 2026-06-22 snapshot; older deltas reflect the prior 2026-04-09 ingest.*

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xeca41281c24451168a37211f0bc2b8645af45092` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://tp.xyz/](https://tp.xyz/) |
| **Twitter** | [@TokenPocket_TP](https://twitter.com/TokenPocket_TP) |
| **Telegram** | [tokenPocket_en](https://t.me/tokenPocket_en) (14,247 members) |
| **GitHub** | [https://github.com/TP-Lab](https://github.com/TP-Lab) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $104,816.00 |
| **Market Cap Rank** | #804 |
| **24h Range** | $0.00634571 — $0.00675399 |
| **Last Updated** | 2026-04-09 |

---

## Competitive position

TokenPocket competes in the **self-custody wallet** market against MetaMask, Trust Wallet, Coinbase Wallet, OKX Wallet, imToken, and Phantom, among others. Its strengths are very broad chain coverage, deep penetration in Asian and TRON/BNB ecosystems, and a mature dApp browser. Its challenges mirror the category: wallet apps are largely free, monetization is difficult, and a tokenized wallet (TPT) must justify its existence beyond what the wallet already does for free — most leading wallets have no token at all. The buyback-and-burn program is the project's attempt to tie token value to business success.

### Comparison vs competitors

| Wallet | Chain coverage | Has a token? | Differentiator |
|---|---|---|---|
| **TokenPocket** (TPT) | Very broad (many EVM + non-EVM, incl. TRON) | **Yes — TPT** (membership + buyback/burn) | Asian/TRON-BNB penetration; tokenized membership |
| **MetaMask** | EVM-focused (+ Snaps extensions) | No | Default Ethereum wallet, largest install base |
| **Trust Wallet** | Very broad multi-chain | TWT (utility) | Binance-affiliated, large mobile base |
| **imToken** | Multi-chain, Asia-strong | No | Long-standing Asian incumbent |
| **Phantom** | Solana-first (+ EVM) | No | Best-in-class Solana UX |

The structural tell: most leading wallets ship **no token at all** because the wallet works without one. TPT must therefore manufacture demand via membership perks and the burn program rather than mandatory usage — a weaker value-accrual position than tokens that gate a chain's gas or staking.

---

## How & Where It Trades

TPT is a BNB Chain BEP-20 (`0xeca4...5092`). The CoinGecko snapshot shows **no major exchange listings recorded** and very thin volume (~$105k/24h on a ~$19M cap), implying most trading is on BNB Chain DEXs. Notes:

- **Thin, DEX-centric liquidity** — expect wide effective spreads and meaningful [[slippage]]; the -9.18% 7d move at the snapshot shows how fast thin wallet tokens reprice in risk-off tape.
- **No durable derivatives market** at this cap; spot-only exposure.
- **Single-chain token** — TPT lives on BNB Chain even though the *wallet* is multi-chain; do not confuse the app's breadth with the token's footprint.

---

## History / Timeline

- **April 2018** — TokenPocket founded (Hong Kong) as a multi-chain self-custody wallet.
- **All-time high $0.1456** on **2021-05-14** (CoinGecko price history); TPT now sits ~95% below that peak.
- **All-time low $0.00012901** on **2020-03-27**.
- **2025-07-01 (project-stated)** — the TokenPocket Foundation began a biannual **buyback-and-burn** program intended to shrink total supply from ~3.466B toward 1B tokens.

> *Dates above are from CoinGecko price history and the project's stated burn-program start; undocumented milestone dates are intentionally omitted rather than invented.*

---

## Risks

- **Token-utility weakness** — the wallet works without TPT; demand depends on membership perks and the burn program rather than mandatory usage.
- **Execution risk on burns** — the deflationary thesis assumes the foundation actually funds and sustains buybacks; a slowdown removes the main demand sink.
- **Competitive pressure** — dominant, well-funded wallets (MetaMask, Trust) that ship no token compete directly.
- **Security/custody surface** — as a self-custody wallet, users bear key-management risk; any app-level vulnerability or supply-chain compromise is reputationally severe.
- **Liquidity / microcap** — sub-$20M cap with modest volume; the -9.18% 7d move shows how quickly thin tokens reprice in risk-off conditions.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed. See History / Timeline above for documented, dated milestones.*

---

## Trading Playbook (bear / Extreme-Fear regime)

- **Regime:** Established Bear Market, Extreme Fear (F&G 21, 2026-06-22). TPT was among the weakest in its cohort at the snapshot (-9.18% 7d), underscoring how thin wallet tokens lead the downside in risk-off conditions.
- **Thesis check:** TPT's only durable demand sink is the **buyback-and-burn** program; the trade is essentially a bet that the foundation funds and sustains burns. Verify actual on-chain burns rather than relying on announcements.
- **Execution:** DEX-only liquidity means size tiny and use limit-style fills to control [[slippage]]; market orders on size will move price.
- **Risk control:** unlimited max supply + weak mandatory utility means no structural floor; pre-define invalidation. See [[risk-management]].

> *Not investment advice.*

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[wallet]]
- [[seed-phrase]]
- [[walletconnect]]
- [[cross-chain]]
- [[slippage]]
- [[risk-management]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.
