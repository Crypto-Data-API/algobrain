---
title: "Liquidity Sniping"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [liquidity-sniping, dex, token-launch, bot-trading, mempool, frontrunning, crypto, algorithmic]
aliases: ["Liquidity Snipe", "Token Launch Sniping", "DEX Sniping Bot"]
strategy_type: algorithmic
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[mev-strategies]]", "[[airdrop-farming]]", "[[defi-yield-farming]]", "[[sentiment-trading]]", "[[algorithmic-trading]]"]
---

# Liquidity Sniping

## Overview

Liquidity sniping is a bot-driven strategy that **buys tokens in the same block (or within milliseconds) of initial liquidity being added** on decentralized exchanges like Uniswap (Ethereum), Raydium (Solana), or PancakeSwap (BSC). When a new token launches, the deployer adds liquidity (a pool of the new token paired with ETH/SOL/USDC) to a DEX. Snipers detect this liquidity addition in the mempool (the queue of pending transactions) and submit a buy transaction with high gas priority to be included in the same or next block -- before any other buyers can push the price up.

The first-mover advantage is enormous: if a token launches at a $50K market cap and quickly pumps to $500K (a 10x), a sniper who bought in the first block captures most of that upside. Manual traders who see the launch on social media minutes later are already buying at inflated prices. In the meme coin and microcap token ecosystem, this speed advantage is the difference between a 10x return and buying the top.

This strategy exists at the intersection of [[mev-strategies]], automated trading, and speculative crypto markets. It is technically demanding (requiring custom bots, mempool monitoring, and gas optimization), extremely high-risk (most new tokens fail, many are scams), and ethically controversial (it disadvantages manual traders). Nevertheless, liquidity sniping has become a significant and persistent feature of DeFi markets, particularly on Solana where sub-second block times enable rapid token launches and snipes.

## How It Works

### The Mempool Pipeline
1. **Token deployer** creates a new ERC-20/SPL token and prepares to add liquidity on a DEX.
2. The **addLiquidity transaction** enters the mempool (Ethereum) or is submitted to validators (Solana).
3. **Sniping bots** monitor the mempool for addLiquidity calls to targeted DEX router contracts (Uniswap V2/V3 Router, Raydium AMM).
4. When detected, the bot **instantly submits a buy transaction** with a higher gas price (on Ethereum) or priority fee to be included in the same or next block.
5. The bot's buy executes at the initial pool price (or very close to it), before the token is publicly known.
6. As organic buyers discover the token (via social media, DEX Screener, Telegram groups), the price pumps.
7. The sniper **sells into the pump** for a profit, often within minutes to hours.

### Technical Components
- **Mempool listener:** WebSocket connection to an Ethereum/Solana node (or a service like Bloxroute, Alchemy, or Helius) monitoring pending transactions.
- **Transaction decoder:** Parses pending transactions to identify addLiquidity calls, extracting the token address, pool parameters, and initial price.
- **Safety checks:** Before buying, the bot performs automated checks: Is the token contract a honeypot (can you sell)? Are there excessive taxes? Is the liquidity locked? Is the deployer a known scammer?
- **Buy executor:** Submits a swap transaction with optimized gas/priority fee to guarantee early block inclusion.
- **Sell logic:** Automated sell at a target profit (2-10x) or trailing stop, or manual sell based on chart/social momentum.

### Solana vs. Ethereum
- **Ethereum:** Mempool-based sniping is well-established. Higher gas costs ($50-500 per snipe). Competition from MEV bots and Flashbots bundles. Block time: 12 seconds.
- **Solana:** No traditional mempool (transactions go directly to validators). Sniping relies on speed (Jito bundles, direct validator connections). Block time: ~400ms. Lower fees ($0.01-$5). More token launches (especially via Pump.fun).

## Rules / Application

### Bot Setup
1. **Deploy a sniping bot** (custom code or commercial tools like Maestro, Banana Gun, BonkBot, or custom Python/Rust bots).
2. **Configure target DEXs:** Uniswap V2/V3 (Ethereum), Raydium/Pump.fun (Solana), PancakeSwap (BSC).
3. **Set buy parameters:** Maximum buy amount per token ($0.1-2 SOL or 0.01-0.5 ETH typically), maximum gas/priority fee, slippage tolerance.
4. **Enable safety checks:** Anti-honeypot verification (simulate a sell transaction before buying), max tax threshold (<10%), liquidity lock verification.

### Risk Management Rules
1. **Never allocate more than 1-5% of portfolio** to sniping across all active positions.
2. **Fixed position size:** Buy the same amount per token ($50-$500). Most tokens go to zero; you need the 10-50x winners to overcome the losses.
3. **Sell rules:** Take 2-3x off the table quickly (within minutes). Let a small position ride for potential 10x+. Close 100% if the token drops 50% from your entry.
4. **Daily loss limit:** Stop sniping for the day if cumulative losses exceed a threshold (e.g., $500).
5. **Blacklist known scammers:** Maintain a database of deployer addresses associated with rug pulls and honeypots.

### Token Evaluation (Seconds-Level Decision)
Even with automation, apply rapid filters:
- Is liquidity > $5K? (Too small = likely a scam)
- Is there a website/social media? (Meme coins without any presence are higher risk)
- Is the contract verified/open-source? (Unverified = honeypot risk)
- Is liquidity locked or burned? (Unlocked = rug pull risk)
- Has the deployer launched and rugged before? (Check deployer history)

## Example

**Setup:** Solana liquidity sniping via Pump.fun using a custom bot.

1. **10:03:15 AM:** Bot detects a new token "CATMOON" migrating from Pump.fun bonding curve to Raydium with $12K liquidity (69 SOL + all CATMOON tokens). Market cap: ~$69K.
2. **10:03:15.4 AM:** Safety check passes: no honeypot, 0% tax, liquidity will be burned on migration. Bot submits buy: 1 SOL ($150) via Jito bundle with $0.01 priority tip.
3. **10:03:15.8 AM:** Buy confirmed in the same block as the liquidity addition. Entry market cap: $69K. Cost basis: $150 for ~0.22% of supply.
4. **10:05 AM:** Token appears on DEX Screener. Crypto Twitter notices. Buyers flood in. Market cap reaches $350K. Position value: ~$750 (5x).
5. **10:05:30 AM:** Sell 50% (0.5 SOL worth) at 5x = $375 profit. Hold remaining.
6. **10:15 AM:** Influencer tweets about CATMOON. Market cap reaches $1.2M. Remaining position worth ~$1,300 (17x on the half).
7. **10:16 AM:** Sell remaining. Total: $375 + $1,300 = $1,675 on a $150 investment. **Net: +$1,525 (10.2x).**
8. **Context:** This is the winning scenario. The same bot may have sniped 20 tokens that day, with 15 going to zero ($150 x 15 = $2,250 lost) and 5 producing profits. Net daily P&L depends on hit rate and average winner size.

## Advantages

- **First-mover advantage** captures the maximum upside from token launches before the broader market discovers them
- On Solana, extremely low transaction costs ($0.01-$5) make high-frequency sniping economically viable
- **Automated execution** removes emotional decision-making and ensures consistent speed
- Some tokens produce 10-100x returns within hours -- outsized winners compensate for the high failure rate
- Rich ecosystem of tools (Maestro, Banana Gun, BonkBot, Photon) has lowered the technical barrier to entry
- Can be combined with [[sentiment-trading]] for post-snipe sell decisions based on social momentum

## Disadvantages

- **Extremely high risk:** The majority of newly launched tokens (estimated 90-99%) fail, are scams, or go to zero within days
- **Rug pull exposure:** Deployers can remove liquidity, enable hidden sell taxes, or blacklist wallets after the snipe
- **Honeypot risk:** Tokens may be coded to prevent selling, trapping the sniper's capital permanently
- **Competition is intense:** Thousands of bots compete for the same opportunities, driving up priority fees and compressing profits
- **MEV/sandwich attacks:** On Ethereum, the sniper may itself get sandwiched by more sophisticated [[mev-strategies|MEV bots]], executing at a worse price
- **Legal gray area:** In some jurisdictions, bot-driven frontrunning of other traders may violate market manipulation regulations
- **Emotional toll:** Watching most positions go to zero while waiting for the occasional winner requires significant psychological resilience
- Profits are highly variable: a week of losses can be followed by a single massive winner, making the strategy difficult to evaluate short-term

## See Also

- [[mev-strategies]] -- broader category of on-chain profit extraction that includes sniping
- [[airdrop-farming]] -- another crypto-native alpha strategy that requires on-chain activity
- [[algorithmic-trading]] -- the automated execution framework that powers sniping bots
- [[sentiment-trading]] -- social momentum analysis for post-snipe sell timing
- [[defi-yield-farming]] -- alternative DeFi profit strategy with lower risk but lower upside
