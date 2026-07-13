---
title: "Rug Pulls"
type: concept
created: 2026-04-14
updated: 2026-07-13
status: good
tags: [crypto, defi, risk-management, security, scams, exploits]
aliases: ["rug pull", "rugpull", "exit scam", "soft rug", "hard rug"]
domain: [risk-management, crypto]
difficulty: beginner
prerequisites: ["[[defi]]"]
related: ["[[smart-contract-risk]]", "[[counterparty-risk]]", "[[defi-hacks-and-exploits]]", "[[2024-meme-coin-supercycle]]", "[[cryptodataapi]]"]
---

A rug pull is a crypto scam where project creators drain liquidity, abandon the project, or otherwise steal user funds after attracting deposits. Unlike technical exploits where attackers find bugs, rug pulls are intentional fraud by insiders. The term comes from the image of "pulling the rug out from under" investors. Rug pulls are the most common form of crypto fraud by *number of incidents* (thousands per year) though individual amounts are typically smaller than protocol exploits. Chainalysis estimated rug pulls accounted for $2.8B in losses in 2021 alone.

## Types of Rug Pulls

### Hard Rug (Technical)

The team uses a built-in backdoor in the smart contract to steal funds:

**Liquidity removal**: The token creator adds initial liquidity to a DEX pool (e.g., Uniswap), waits for buyers to accumulate, then removes all liquidity — crashing the token to zero. Buyers are left holding worthless tokens with no liquidity to sell into.

**Hidden mint function**: The contract contains an owner-only function to mint unlimited tokens. The team mints a massive supply and sells it, diluting all holders.

**Transfer restrictions**: The contract allows anyone to buy but only the owner to sell (a "honeypot"). Buyers discover they cannot sell only after purchasing.

**Proxy contract manipulation**: The project deploys an upgradeable proxy contract, initially with legitimate logic. After attracting deposits, the team upgrades the contract to drain all funds.

### Soft Rug (Abandonment)

The team gradually abandons the project without a single dramatic theft:

- Stop developing the product
- Stop communicating with the community
- Sell their token allocation slowly over weeks/months
- Let the project die a slow death

Soft rugs are harder to prosecute because no single action constitutes fraud — the team simply "lost interest." They are extremely common in meme coin and NFT markets.

### Slow Rug

A hybrid where the team extracts value over time through excessive token emissions, inflated team allocations, or "ecosystem fund" spending that benefits insiders. The project may continue operating while insiders steadily sell their allocations.

## Notable Rug Pulls

| Date | Project | Amount | Type | Details |
|------|---------|--------|------|---------|
| 2020-09 | SushiSwap (Chef Nomi) | $13M | Soft rug → reversal | Chef Nomi sold dev fund tokens; community pressure forced return. SushiSwap survived |
| 2021-04 | TurtleDex | $2.5M | Hard rug | BSC token — team removed liquidity and deleted social media |
| 2021-06 | Iron Finance / Titan | $2B TVL collapse | Soft rug / bank run | Algorithmic stablecoin death spiral; Mark Cuban was an investor |
| 2021-10 | AnubisDAO | $60M | Hard rug | Raised $60M in an Olympus DAO fork; funds drained within 20 hours of launch |
| 2021-10 | Squid Game Token | $3.4M | Honeypot | Buyers could not sell; team dumped their allocation |
| 2021-11 | Evolved Apes | $2.7M | NFT rug | Creator disappeared with mint proceeds |
| 2022-04 | Frosties NFT | $1.3M | NFT rug | Creators arrested by DOJ — first NFT rug pull prosecution |
| 2024 | Various meme coins | $100M+ collectively | Pump-and-dump / soft rug | The [[2024-meme-coin-supercycle|meme coin supercycle]] produced hundreds of short-lived tokens |

## Red Flags

### Contract Red Flags
- **Unverified source code** on the block explorer (cannot inspect the contract logic)
- **Owner-only mint or transfer functions** without time locks
- **No liquidity lock** (the LP tokens are not locked in a time-lock contract — the creator can pull them at any time)
- **Proxy/upgradeable contracts** without governance controls
- **Hidden fees** (high sell taxes, blacklist functions, anti-bot measures that actually prevent selling)

### Team Red Flags
- **Anonymous team** with no verifiable track record (anonymity alone isn't a red flag — many legitimate DeFi teams are anonymous — but combined with other flags, it increases risk)
- **No audits** or audits from unknown firms
- **Unrealistic APY promises** (1,000%+ yields with no clear source of revenue)
- **Aggressive marketing** with paid influencer shilling and artificial urgency ("launch in 2 hours!")
- **Locked Discord/Telegram** where only admins can post
- **Copied/forked code** with minimal modifications

### Market Red Flags
- **Concentrated token ownership** — if the top 5 wallets hold >50% of supply, any of them can crash the price
- **Low liquidity** relative to market cap — a $50M market cap with $200K liquidity means large sells are impossible
- **Suspicious price action** — straight-up chart with no pullbacks suggests wash trading

## Defenses

### Before Buying
1. **Read the contract** — check for owner-only functions, minting, blacklists, proxy patterns (or use tools like Token Sniffer, GoPlus, De.Fi Scanner)
2. **Check liquidity locks** — is LP locked in a time-lock contract? For how long? (Use DexScreener, Unicrypt, Team Finance)
3. **Verify the team** — do they have a track record? Have they been doxxed? Do they have real social media history?
4. **Check token distribution** — use Etherscan/BSCScan to see holder concentration
5. **Wait** — most rug pulls happen within the first 48 hours of launch. Waiting reduces risk significantly

### After Buying
1. **Set stop losses** or take profits early — don't let greed override risk management
2. **Monitor team activity** — if social media goes quiet or the team stops shipping, consider exiting
3. **Watch for LP unlocks** — if the liquidity lock expires, the team can pull at that date

## Legal Landscape

Rug pulls are increasingly prosecuted:
- **U.S. DOJ** prosecuted the Frosties NFT rug pull creators (arrested 2022, convicted)
- **SEC** has brought cases against crypto promoters for securities fraud via rug pulls
- **CFTC** has jurisdiction over commodity-classified token fraud
- In many jurisdictions, rug pulls constitute wire fraud, securities fraud, or theft — all criminal offenses

However, prosecution is difficult when teams are anonymous and funds are laundered through mixers or cross-chain bridges.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].

## Related

- [[smart-contract-risk]] — hard rugs exploit built-in contract backdoors
- [[counterparty-risk]] — rug pulls are a form of counterparty risk (trusting the team)
- [[2024-meme-coin-supercycle]] — the meme coin era produced hundreds of rug pulls
- [[defi-hacks-and-exploits]] — master timeline (rug pulls vs. technical exploits)

## Sources

_Content based on Chainalysis crypto crime reports, DOJ prosecution filings, and public blockchain analysis. No raw sources ingested._
