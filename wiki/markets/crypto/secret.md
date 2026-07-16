---
title: "Secret"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi]
aliases: ["SCRT", "Secret Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://scrt.network"
related: ["[[cosmos]]", "[[crypto-markets]]", "[[layer-1]]", "[[privacy-coins]]", "[[smart-contracts]]", "[[trusted-execution-environment]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Secret

**Secret** (SCRT) is the native staking and gas token of [[secret|Secret Network]], a privacy-preserving [[layer-1|layer-1]] blockchain built with the [[cosmos|Cosmos SDK]] and Tendermint proof-of-stake consensus. Its distinguishing feature is **"secret contracts"** — [[smart-contracts]] whose inputs, outputs, and internal state remain encrypted, executed inside [[trusted-execution-environment|trusted execution environments]] (TEEs, specifically Intel SGX enclaves) run by validators. This makes Secret one of the few general-purpose smart-contract platforms offering programmable, on-chain data privacy rather than just transaction-level anonymity like most [[privacy-coins]]. It ranks **#832** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* SCRT trades at **$0.057692**, market cap **$19,820,301** (rank **#832**), down **-1.68%** over 24h and down **-4.93%** over 7 days, amid a broad risk-off regime (BTC ~$64,166; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SCRT |
| **Market Cap Rank** | #832 |
| **Market Cap** | $19,820,301 |
| **Current Price** | $0.057692 |
| **24h Change** | -1.68% |
| **7d Change** | -4.93% |
| **Categories** | Privacy Blockchain, Smart Contract Platform, Cosmos Ecosystem, Layer 1 (L1), Osmosis Ecosystem, Infrastructure |
| **Website** | [https://scrt.network](https://scrt.network) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Secret Network is a decentralized network for private, secure computation. "Secret nodes" (validators) perform generalizable computations over encrypted data, allowing smart contracts — "secret contracts" — to take private and sensitive data as inputs without exposing it to validators, observers, or even the contract's own counterparties. The project's emphasis is **computational privacy**, not merely transactional privacy: balances, contract state, and message payloads can be kept confidential by default. Developers build privacy-preserving "Secret Apps" (sApps) for use cases spanning [[decentralized-finance|DeFi]], NFTs with private content, access control, gaming, and confidential data markets.

The network traces its roots to the **Enigma** project (founded by MIT researchers, ~2015–2017) and later relaunched as Secret Network in 2020. It is supported by independent contributors including SCRT Labs (formerly Enigma), the Secret Foundation, and a broad validator set.

---

## Architecture & Consensus

- **Layer-1 chain** built on the [[cosmos|Cosmos SDK]] with Tendermint BFT [[proof-of-stake]] consensus; interoperable with the wider Cosmos ecosystem via [[inter-blockchain-communication|IBC]] (e.g., bridges to Osmosis).
- **Privacy via TEEs:** secret contracts execute inside [[trusted-execution-environment|trusted execution environments]] (Intel SGX secure enclaves). Encrypted inputs are decrypted only inside the enclave, computed on, and re-encrypted — so the host validator never sees plaintext.
- **Encrypted state:** contract state is stored encrypted on-chain; only authorized "viewing keys" or permits can decrypt a user's own data.
- **CosmWasm-based** smart-contract environment (Rust), extended with privacy primitives.

This TEE-based design is a deliberate trade-off versus pure-cryptography approaches (zero-knowledge proofs, fully homomorphic encryption): it delivers general-purpose private compute with practical performance, at the cost of trusting the hardware vendor's enclave and its side-channel resistance (see [[#Risks]]).

### Viewing keys, permits, and SNIP-20 tokens

Because contract state is encrypted by default, Secret introduces explicit mechanisms for *authorized* disclosure:

- **Viewing keys** — a user-set secret that lets an account (or an authorized app) decrypt and read its own data from a contract (e.g., a private token balance). Without it, even the owner's balance is opaque on-chain.
- **Query permits** — signature-based, key-less alternatives to viewing keys for read access, improving UX.
- **SNIP-20 / SNIP-721** — Secret's privacy-preserving token standards (analogous to ERC-20 / ERC-721) where balances and transfers are encrypted, enabling private fungible tokens and NFTs with hidden content/metadata.

A flagship application of this is **Secret Tokens (sTokens)** — privacy-wrapped versions of public assets (e.g., sSCRT, bridged sTokens) that move confidentially within the network.

### Comparison with peer privacy / confidential-compute networks

| Project | Privacy primitive | Base layer | Scope of privacy | Token role |
|---|---|---|---|---|
| **Secret (SCRT)** | TEE (Intel SGX) | [[cosmos\|Cosmos]] [[layer-1\|L1]] (Tendermint PoS) | Programmable private **smart contracts** (state, I/O encrypted) | Gas, staking, governance |
| [[pha\|Phala (PHA)]] | TEE (SGX/TDX, confidential GPU) | [[polkadot\|Polkadot]] heritage / ERC-20 | Decentralized confidential **compute** / AI agents | Staking, worker bond, payment, governance |
| [[coti\|COTI (COTI)]] | Garbled Circuits / MPC | Confidentiality layer on [[ethereum\|Ethereum]] | Confidential transactions & compute | Fees, staking, governance |
| Oasis (ROSE) | TEE (SGX) | Standalone L1 | Confidential EVM (Sapphire ParaTime) | Gas, staking, governance |
| Monero / Zcash | Ring signatures / ZK | Standalone L1 (UTXO) | **Transaction-level** anonymity only (no smart contracts) | Currency |

Secret's niche is **general-purpose programmable privacy** (private smart contracts) within the [[cosmos|Cosmos]]/IBC ecosystem — broader than transaction-only [[privacy-coins]] like Monero/Zcash, and distinct from [[coti|COTI]]'s cryptographic (no-hardware-trust) approach. It shares the TEE/hardware-trust trade-off with [[pha|Phala]] and Oasis.

---

## What the SCRT Token Does

- **Gas:** transaction and contract-execution fees are paid in SCRT.
- **Staking:** SCRT is bonded to validators to secure the [[proof-of-stake]] chain; stakers earn block rewards and a share of fees, subject to slashing.
- **Governance:** SCRT holders vote on on-chain proposals (parameter changes, treasury spending, upgrades).

### Staking and value accrual

As a Cosmos-SDK chain, Secret runs **bonded [[proof-of-stake]]**: SCRT is delegated to validators, who produce blocks and run the SGX enclaves that execute secret contracts. Stakers earn newly minted SCRT plus a share of transaction fees, with an **unlimited max supply** (inflationary), so nominal yield is partly offset by issuance. Bonded stake is **slashable** for double-signing or downtime, and unbonding has a lock-up (typically ~21 days in Cosmos chains) that reduces liquid float. Value accrual depends on (1) demand for blockspace/private compute generating fees, and (2) the staking ratio locking supply; with inflationary issuance, real value accrual requires fee and usage growth to outpace dilution. Confirm current inflation parameters and the staking ratio against on-chain data.

---

## Governance

SCRT holders govern Secret Network on-chain via the standard Cosmos governance module: proposals (parameter changes, software upgrades, community-pool spending, signaling) are submitted with a deposit and voted on by **staked SCRT**, with options for Yes / No / No-with-Veto / Abstain and a veto threshold that can reject and burn the deposit of harmful proposals. Validators vote on behalf of delegators unless a delegator overrides them. Governance has historically directed the community pool toward ecosystem grants, privacy R&D, and protocol upgrades. As with most small/mid-cap PoS chains, influence concentrates among large validators and active delegators.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 336.91M SCRT |
| **Total Supply** | 351.96M SCRT |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.31M |
| **Market Cap / FDV Ratio** | 0.96 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $10.38 (2021-10-28) |
| **Current vs ATH** | -99.17% |
| **All-Time Low** | $0.0706 (2026-03-29) |
| **Current vs ATL** | +22.07% |
| **24h Change** | -3.78% |
| **7d Change** | +12.44% |
| **30d Change** | +12.29% |
| **1y Change** | -45.72% |

---

## Platform & Chain Information

**Native Chain:** Secret

### Contract Addresses

| Chain | Address |
|---|---|
| Secret | `secret1k0jntykt7e4g3y88ltc60czgjuqdy4c9e8fzek` |
| Osmosis | `ibc/0954E1C28EB7AF5B72D24F3BC2B47BBB2FDF91BDDFD57B74B99E133AED40972A` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SCRT/USDT | N/A |
| Kraken | SCRT/USD | N/A |
| KuCoin | SCRT/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://scrt.network](https://scrt.network) |
| **Twitter** | [@secretnetwork](https://twitter.com/secretnetwork) |
| **Telegram** | [scrtcommunity](https://t.me/scrtcommunity) (7,199 members) |
| **Discord** | [https://discord.com/invite/SJK32GY](https://discord.com/invite/SJK32GY) |
| **GitHub** | [https://github.com/scrtlabs/SecretNetwork](https://github.com/scrtlabs/SecretNetwork) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 579 |
| **GitHub Forks** | 229 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 783 |
| **Contributors** | 54 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.63M |
| **Market Cap Rank** | #810 |
| **24h Range** | $0.0860 — $0.0933 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **Enigma origins (2015–2017):** the project began as **Enigma**, founded by MIT researchers, with a 2017 token sale (ENG). The vision was a "privacy layer" for decentralized data; the team (later SCRT Labs) iterated from an Ethereum-based design toward a dedicated TEE-based chain.
- **Secret Network mainnet (2020):** Enigma relaunched as **Secret Network**, a Cosmos-SDK [[layer-1|L1]] with SGX-based "secret contracts," and ENG holders could migrate to SCRT. The Secret Foundation and SCRT Labs supported growth alongside an open validator set.
- **2021 bull run:** SCRT reached its all-time high of **$10.38** on 2021-10-28 amid heightened interest in privacy infrastructure and Cosmos DeFi. It has since fallen more than 99% from that peak, in line with the broader collapse of small-cap altcoins.
- **TEE / side-channel scrutiny:** because secret contracts depend on Intel SGX, the network's confidentiality guarantees are periodically re-examined by security researchers as new SGX vulnerabilities and side-channel attacks are disclosed industry-wide. This is an inherent, ongoing risk for any TEE-based privacy system. Researchers have previously demonstrated SGX-related extraction risks affecting SGX-based chains, prompting mitigations.
- **2026 small-cap drawdown:** SCRT printed an all-time low of **$0.0706** on 2026-03-29 in the broad washout, then partially recovered; as of 2026-06-22 it is **-4.93% over 7 days** and **-1.68% on the day** in an Extreme-Fear market (BTC ~$64,166).

> *Notable events will continue to be added through the wiki's source ingestion workflow.*

---

## Risks

- **Hardware-trust dependency:** privacy relies on the integrity of Intel SGX enclaves. Disclosed SGX side-channel vulnerabilities (an industry-wide pattern) could, in principle, weaken confidentiality until patched — the same structural risk faced by TEE peers [[pha|Phala]] and Oasis. This is a *trust-the-vendor* model, unlike pure-cryptography ([[zero-knowledge-proof|ZK]]/MPC/FHE) approaches such as [[coti|COTI]]'s.
- **Regulatory risk:** like all [[privacy-coins]] and privacy infrastructure, Secret faces potential exchange delistings and regulatory pressure in jurisdictions hostile to on-chain privacy; privacy assets have been delisted from some exchanges in certain regions.
- **Inflationary issuance:** SCRT has no fixed max supply; staking yield is partly nominal, and value accrual requires usage/fee growth to outpace dilution.
- **Competition:** programmable-privacy is contested by [[coti|COTI]] (Garbled Circuits), Oasis Sapphire, FHE chains, and [[zero-knowledge-proof|ZK]]-based privacy L2s; Secret must sustain a developer and app ecosystem to stay relevant.
- **Small-cap liquidity:** at a ~$20M market cap and rank #832, SCRT is thinly traded and highly volatile; large orders can move price materially.
- **Bear-regime drawdown:** down >99% from its 2021 ATH; survival depends on continued developer activity and ecosystem demand.

> Not investment advice. Figures are point-in-time; verify project, on-chain, and TEE-security claims independently.

---

## Trading Profile

### Venues & liquidity

SCRT is tradable on [[binance]] — both **spot** (SCRT/USDT) and a **USD-margined [[perpetual-futures|perpetual]]** with [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations|liquidation]] data. It is **not** listed on Hyperliquid, so Binance is the primary — effectively sole — leveraged venue. This concentration means the Binance perp order book and funding print set the reference for all leveraged flow: there is no on-chain perp DEX to arbitrage against or fall back on, and a single-venue outage or delisting would remove leveraged access entirely. Given the ~$20M market cap and thin spot depth, available leverage is modest and liquidity is shallow — position sizing must account for wide effective spreads and slippage on market orders, and execution favors patient limit orders and scaled entries over aggressive size.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on SCRT when the single-venue rate runs persistently positive or negative, delta-hedged against spot.
- [[cash-and-carry]] — hold SCRT spot against a short perp to capture basis/funding when the curve is in contango, exploiting the one-venue funding skew.
- [[liquidation-cascade-fade]] — thin books make SCRT prone to sharp, self-reinforcing liquidation wicks on the Binance perp; fade the overshoot after cascades clear.
- [[range-mean-reversion]] — low-cap SCRT often chops in a range between catalysts; mean-revert the extremes when momentum is absent.
- [[breakout-and-retest]] — trade confirmed breakouts of consolidation on volume expansion, using the retest for defined risk given whippy low-liquidity price action.
- [[oi-confirmed-trend]] — use Binance open-interest changes to distinguish real trend continuation from thin-book fake-outs before committing size.

### Volatility & regime character

SCRT is a **small-cap** ($20M-range), high-beta infrastructure/privacy [[layer-1|L1]] token with sharp, reflexive moves driven by low float and thin liquidity rather than memecoin-style hype. It is **highly correlated to BTC/ETH risk regime** — it sells off hard in risk-off/Extreme-Fear conditions and rallies with broad altcoin beta — but layers on idiosyncratic swings tied to privacy-sector narrative and Cosmos-ecosystem flows. Expect large percentage drawdowns and rallies on modest notional volume; realized volatility is elevated and clusters around catalysts.

### Risk flags

- **Venue concentration:** Binance is the only meaningful leveraged venue and a major spot venue; a delisting or outage is an outsized single point of failure — acute for [[privacy-coins]], which face recurring exchange-delisting and regulatory pressure.
- **Liquidity:** ~$20M cap and thin depth mean large orders move price materially and stops can slip badly during cascades.
- **Inflationary emissions:** SCRT has no max supply; ongoing issuance dilutes holders and can pressure price absent usage growth.
- **Narrative dependence:** valuation hinges on the privacy/confidential-compute narrative and TEE-security perception; SGX side-channel disclosures can trigger sentiment-driven repricing.
- **Regulatory:** as privacy infrastructure, SCRT carries elevated delisting/regulatory risk in jurisdictions hostile to on-chain privacy.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SCRTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SCRTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SCRT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SCRT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SCRTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SCRTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SCRT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[privacy-coins]]
- [[trusted-execution-environment]]
- [[cosmos]]
- [[smart-contracts]]
- [[proof-of-stake]]
- [[pha]]
- [[coti]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); BTC ~$64,166, Fear & Greed 21 / Extreme Fear.
- General market knowledge; no additional specific wiki source ingested yet.
