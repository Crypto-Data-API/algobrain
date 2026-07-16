---
title: "VVS Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["VVS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://vvs.finance/"
related: ["[[automated-market-maker]]", "[[cronos]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[defi]]", "[[ethereum]]", "[[pancakeswap]]"]
---

# VVS Finance

**VVS Finance** (ticker **VVS**) is a [[decentralized-exchange|decentralized exchange]] ([[dex|DEX]]) and [[automated-market-maker|automated market maker]] (AMM) built primarily on the [[cronos|Cronos]] chain, the EVM-compatible network associated with Crypto.com. The protocol also has a deployment on [[ethereum|Ethereum]]. VVS is designed as a "sparkly simple" yield-farming and swapping venue, modeled on the [[pancakeswap|PancakeSwap]]/SushiSwap AMM template, and the VVS token is its governance and liquidity-mining reward token. It is the flagship native AMM of the Cronos ecosystem.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | VVS |
| **Current Price** | $0.00000102 |
| **Market Cap** | $44.58M |
| **Market Cap Rank** | #492 |
| **24h Volume** | $23,478 |
| **24h Change** | +0.21% |
| **7d Change** | -2.70% |
| **All-Time High** | $0.00033093 (2021-11-15) — now ~-99.7% |
| **All-Time Low** | $0.000000986 |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

The 2026-06-20 snapshot lands during a broad crypto risk-off phase: the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (Extreme Fear)** and market commentary characterizes the backdrop as an **established bear market**. VVS's 24-hour turnover of ~$23K against a ~$44.6M cap is extremely thin (turnover ~0.05% of cap), signalling very low liquidity and elevated slippage risk for any sizable position. The token trades essentially on top of its all-time low.

---

## Tokenomics & Supply

VVS uses a deflationary-by-design but very high nominal supply structure (denominated in trillions of tokens, hence the sub-cent unit price).

| Metric | Value |
|---|---|
| **Circulating Supply** | 43.55T VVS |
| **Total Supply** | 95.11T VVS |
| **Max Supply** | 100.00T VVS |
| **Fully Diluted Valuation** | ~$102M (price × max supply) |
| **Market Cap / FDV** | ~0.44 |

> **Dilution flag:** the large gap between circulating supply (43.55T, ~44% of max) and max supply (100T) means roughly **56% of the eventual token base is not yet in circulation**. Emissions to liquidity miners and the gap to FDV represent ongoing dilution pressure; new VVS minted as farming rewards is structural sell-side supply that holders must absorb.

The token captures value through trading-fee accrual, staking ("VVS Mine" / xVVS-style vaults), and use as the reward asset that bootstraps liquidity on the DEX. Like most farm tokens, value capture is reflexive: emissions attract liquidity, liquidity generates fees, fees nominally back the token — but if incentive yield outpaces fee revenue, net inflation erodes price.

---

## How & Where It Trades

**Spot — centralized:**
- Crypto.com Exchange (VVS/USD)

**Spot — decentralized:**
- VVS Finance itself (native AMM on Cronos)
- [[decentralized-exchange|Uniswap V2]] on Ethereum (VVS / USDC)

**Derivatives:** No major perpetual or futures listing for VVS is recorded in the 2026-06-20 snapshot (no Hyperliquid perp, no funding-rate or open-interest data). Exposure is effectively spot-only, concentrated on the Crypto.com ecosystem.

Because daily volume is only tens of thousands of dollars, VVS is best viewed as a thin, ecosystem-bound altcoin: price is highly sensitive to a small number of orders, and execution on anything beyond a small ticket will move the market.

---

## Use Case, Narrative & Category

VVS Finance sits in the **DeFi / DEX / AMM** category and is part of the **Cronos** and **Ethereum** ecosystems. Its core functions:

- **Swapping** — constant-product AMM for token pairs on Cronos
- **Yield farming** — liquidity providers earn VVS emissions
- **Staking / vaults** — single-asset and LP staking for additional yield
- **Governance** — token-weighted voting on protocol parameters

Strategically, VVS is the flagship DEX for the Cronos chain, giving it a role analogous to [[pancakeswap|PancakeSwap]] on BNB Chain. Its fortunes are tightly coupled to Cronos network activity and to the broader Crypto.com ecosystem.

---

## Peer Comparison

VVS is a single-chain AMM/farm token; its natural peers are other chain-flagship DEX tokens. Figures from the 2026-06-20 snapshot where available (qualitative otherwise).

| Token | Chain | Model | MC Rank | Market Cap | Note |
|---|---|---|---|---|---|
| **VVS** | [[cronos\|Cronos]] | AMM / farm | #492 | ~$44.6M | Flagship Cronos DEX; very thin volume |
| [[pancakeswap\|CAKE]] | BNB Chain | AMM / farm | top-100 tier | (much larger) | Category template; deepest farm liquidity |
| [[velodrome-finance\|VELO (Velodrome)]] | [[base\|Base]]/Optimism | ve(3,3) AMM | #753 | ~$23.1M | ve-tokenomics model; not the same VELO as Velo Protocol |
| Uniswap (UNI) | [[ethereum\|Ethereum]]/multi | AMM | top-tier | (much larger) | No native emissions; fee-switch debate |

VVS's distinguishing weakness in this peer set is **liquidity**: its daily turnover is in the tens of thousands of dollars, orders of magnitude below the multichain AMM leaders.

---

## Valuation Framing (Qualitative)

- **MC/FDV ~0.44** — roughly half the token base is unminted; on a fully-diluted basis VVS is ~2.3x its current cap, a meaningful overhang for a thin-float farm token.
- **Fee-to-emission balance** — the key fundamental question is whether trading fees on Cronos cover the VVS paid out as farm rewards. In a low-activity bear market this balance typically runs net-inflationary.
- **Beta to Cronos / Crypto.com** — VVS is effectively a leveraged proxy for Cronos chain activity; it has no independent demand driver outside that ecosystem.
- **Liquidity discount** — with ~$23K daily volume, any valuation must price in a steep liquidity/exit-risk discount versus larger AMM peers.

This is framing, not a price target — no valuation model in the wiki produces a fair-value estimate for VVS.

---

## Notable History

- **2021** — Launched on Cronos as the chain's primary AMM during the Crypto.com ecosystem expansion. All-time high of **$0.00033093** reached on **2021-11-15** during the bull-market peak.
- **2021–2026** — Long structural drawdown in line with the altcoin/DeFi bear market; the current price is roughly **-99.7%** from ATH.
- **2026-06-20** — Trading near all-time-low territory (ATL ~$0.000000986), essentially flat on the day (+0.21%) and down ~2.7% on the week amid extreme-fear market conditions.

---

## Risks

- **Liquidity risk** — ~$42K of daily volume is dangerously thin; large orders will incur heavy slippage and exit liquidity is poor.
- **Dilution** — ~56% of max supply is not yet circulating; continued emissions to farmers dilute holders.
- **Ecosystem concentration** — value is tied to Cronos / Crypto.com adoption; weakness there flows directly to VVS.
- **Smart-contract risk** — as an AMM/yield protocol, VVS is exposed to contract exploits and impermanent loss for LPs.
- **Macro / regime risk** — in an established bear market with Fear & Greed at 23, low-cap DeFi tokens are typically among the worst performers.

---

## Platform & Chain Information

**Native Chain:** Cronos

### Contract Addresses

| Chain | Address |
|---|---|
| Cronos | `0x2d03bece6747adc00e1a131bba1469c15fd11e03` |
| Ethereum | `0x839e71613f9aa06e5701cf6de63e303616b0dde3` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://vvs.finance/](https://vvs.finance/) |
| **Twitter** | [@VVS_finance](https://twitter.com/VVS_finance) |
| **Telegram** | [VVSFinance](https://t.me/VVSFinance) |
| **Discord** | [https://discord.com/invite/V2957zMsmg](https://discord.com/invite/V2957zMsmg) |

---

## See Also

- [[crypto-markets]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[cronos]]
- [[ethereum]]
- [[defi]]
- [[pancakeswap]]
- [[velodrome-finance]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko top-1000 markets snapshot).

