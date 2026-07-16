#!/usr/bin/env python3
"""
Generate wiki markdown pages for top 1000 cryptocurrencies from CoinGecko data.

Reads raw JSON from raw/data/crypto-coins/, generates or merges wiki pages
into wiki/markets/crypto/, and updates indexes + log.

Usage:
    python tools/generate_crypto_pages.py
    python tools/generate_crypto_pages.py --dry-run   # preview without writing
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "raw" / "data" / "crypto-coins"
WIKI_CRYPTO = ROOT / "wiki" / "markets" / "crypto"
WIKI_SOURCES = ROOT / "wiki" / "sources"
WIKI_ROOT = ROOT / "wiki"

TODAY = datetime.utcnow().strftime("%Y-%m-%d")
SOURCE_ID = f"coingecko-top-1000-{TODAY}"

# Files that are NOT coin pages — skip during merge detection
NON_COIN_FILES = {
    "crypto-overview", "crypto-markets", "crypto-winter", "crypto", "cryptocurrency",
    "halving", "staking", "mempool", "layer-2", "flashbots", "bitcoin-etfs",
    "nft", "stablecoins", "stablecoin-yields", "other-stablecoins",
    "hyperliquid-market-snapshot-2026-04-06",
    # NFT collection pages
    "bored-ape-yacht-club", "cryptopunks", "azuki", "cool-cats", "doodles",
    "moonbirds", "cryptokitties", "meebits", "pudgy-penguins", "art-blocks",
    "autoglyphs", "world-of-women", "curio-cards", "rare-pepes", "mooncats",
    "etherrock", "nba-top-shot",
}

# Out-of-scope: tokenized single-name equities / equity ETFs (repo rule: no equity content).
# In scope and NOT filtered: tokenized commodities (gold), treasuries/T-bills, RWA funds, stablecoins.
EQUITY_NAME_HINTS = ("xstock", "bstock", "-tokenized-stock", "tokenized-stock", "tokenized-etf")


def is_out_of_scope_equity(coin_id, name, categories):
    """True for tokenized single-name stocks and equity-index ETFs (crypto/BTC ETFs stay)."""
    cats = [c.lower() for c in (categories or [])]
    blob = f"{coin_id} {name or ''}".lower()
    if "tokenized stock" in cats:
        return True
    if any(h in blob for h in EQUITY_NAME_HINTS):
        return True
    cat_join = " ".join(cats)
    if ("tokenized etf" in cat_join or "tokenized-etf" in blob) and not any(
        k in blob for k in ("bitcoin", "btc", "ether", "eth", "crypto")
    ):
        return True
    return False

# CoinGecko category -> wiki tags mapping
CATEGORY_TAG_MAP = {
    "layer-1": "crypto",
    "layer-2": "crypto",
    "smart-contract-platform": "crypto",
    "decentralized-finance-defi": "defi",
    "decentralized-exchange": "defi",
    "lending-borrowing": "defi",
    "yield-farming": "defi",
    "liquid-staking-tokens": "defi",
    "meme-token": "crypto",
    "stablecoins": "crypto",
    "exchange-based-tokens": "crypto",
    "governance": "crypto",
    "oracle": "crypto",
    "cross-chain": "crypto",
    "gaming": "crypto",
    "metaverse": "crypto",
    "nft": "nft",
    "privacy-coins": "crypto",
    "storage": "crypto",
    "infrastructure": "crypto",
    "artificial-intelligence": "ai-trading",
    "real-world-assets": "crypto",
}

# ---------------------------------------------------------------------------
# Helpers — number formatting
# ---------------------------------------------------------------------------

def fmt_usd(val):
    """Format number as USD string."""
    if val is None:
        return "N/A"
    if abs(val) >= 1e12:
        return f"${val/1e12:,.2f}T"
    if abs(val) >= 1e9:
        return f"${val/1e9:,.2f}B"
    if abs(val) >= 1e6:
        return f"${val/1e6:,.2f}M"
    if abs(val) >= 1e3:
        return f"${val:,.2f}"
    if abs(val) >= 1:
        return f"${val:,.2f}"
    if abs(val) >= 0.01:
        return f"${val:,.4f}"
    return f"${val:,.8f}"


def fmt_num(val):
    """Format large number with commas."""
    if val is None:
        return "N/A"
    if abs(val) >= 1e12:
        return f"{val/1e12:,.2f}T"
    if abs(val) >= 1e9:
        return f"{val/1e9:,.2f}B"
    if abs(val) >= 1e6:
        return f"{val/1e6:,.2f}M"
    return f"{val:,.0f}"


def fmt_pct(val):
    """Format percentage."""
    if val is None:
        return "N/A"
    return f"{val:+.2f}%"


def fmt_date(iso_str):
    """Extract YYYY-MM-DD from ISO date string."""
    if not iso_str:
        return "N/A"
    return iso_str[:10]


def strip_html(text):
    """Remove HTML tags from text."""
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", "", text)
    clean = re.sub(r"\n{3,}", "\n\n", clean)
    return clean.strip()


# ---------------------------------------------------------------------------
# Helpers — frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    """Parse YAML frontmatter and body from markdown string."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    # Simple YAML parser for our flat frontmatter
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^(\w[\w-]*)\s*:\s*(.+)$', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            # Handle quoted strings
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            # Handle lists
            elif val.startswith("["):
                val = val  # keep as string for simplicity
            fm[key] = val
    return fm, body


def parse_sections(body):
    """Split markdown body into sections by ## headings."""
    sections = {}
    current_heading = "__lead__"
    current_lines = []

    for line in body.split("\n"):
        if line.startswith("## "):
            sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)

    sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def get_status(fm):
    """Get page status from frontmatter."""
    return fm.get("status", "stub")


# ---------------------------------------------------------------------------
# Helpers — Hyperliquid data
# ---------------------------------------------------------------------------

def load_hyperliquid_assets():
    """Load Hyperliquid asset list and return dict of {SYMBOL: data}."""
    hl_file = DATA_DIR / "_hyperliquid-assets.json"
    if not hl_file.exists():
        return {}

    data = json.loads(hl_file.read_text(encoding="utf-8"))
    hl_map = {}

    if isinstance(data, dict):
        # CryptoData API returns {prices: {SYM: price, ...}, funding_oi: {...}}
        prices = data.get("prices", {})
        funding_oi = data.get("funding_oi", {})

        for sym, price in prices.items():
            if sym.startswith("@"):
                continue  # skip spot tokens, only want perps
            info = {"price": price}
            if sym in funding_oi:
                info.update(funding_oi[sym] if isinstance(funding_oi[sym], dict) else {})
            hl_map[sym.upper()] = info

    return hl_map


# ---------------------------------------------------------------------------
# Page generation from API data
# ---------------------------------------------------------------------------

def get_safe(data, *keys, default=None):
    """Safely navigate nested dict."""
    val = data
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            return default
        if val is None:
            return default
    return val


def map_tags(categories):
    """Map CoinGecko categories to wiki tags."""
    tags = {"crypto"}
    if not categories:
        return sorted(tags)
    for cat in categories:
        if not cat:
            continue
        slug = cat.lower().replace(" ", "-").replace("(", "").replace(")", "")
        mapped = CATEGORY_TAG_MAP.get(slug)
        if mapped:
            tags.add(mapped)
        # Also add simplified category as tag if it's in approved list
        simple = slug.replace("-", "-")
        approved = {
            "bitcoin", "ethereum", "altcoins", "defi", "nft",
            "algorithmic", "quantitative", "ai-trading", "machine-learning",
        }
        if simple in approved:
            tags.add(simple)
    return sorted(tags)


def build_related_links(data, hl_assets):
    """Build wikilinks to related pages based on platform and category."""
    links = ['[[crypto-markets]]']
    platform = get_safe(data, "asset_platform_id")
    if platform:
        chain_map = {
            "ethereum": "ethereum",
            "binance-smart-chain": "bnb",
            "solana": "solana",
            "polygon-pos": "polygon",
            "arbitrum-one": "arbitrum",
            "avalanche": "avalanche",
            "optimistic-ethereum": "optimism",
            "base": "base",
        }
        wiki_name = chain_map.get(platform)
        if wiki_name:
            links.append(f"[[{wiki_name}]]")
    return links


def extract_exchange_listings(tickers, symbol):
    """Extract notable exchange listings from tickers data."""
    if not tickers:
        return [], []

    cex_rows = []
    dex_rows = []
    seen_cex = set()
    seen_dex = set()

    # Priority exchanges for CEX
    priority_cex = ["binance", "coinbase", "kraken", "bybit", "okx", "upbit",
                    "bitget", "gate_io", "kucoin", "htx", "mexc", "crypto_com"]

    for t in tickers:
        market = t.get("market", {})
        exchange_id = market.get("identifier", "")
        exchange_name = market.get("name", exchange_id)
        base = t.get("base", "")
        target = t.get("target", "")
        trust = t.get("trust_score", "")
        pair = f"{base}/{target}"

        # CEX
        if exchange_id in priority_cex and exchange_id not in seen_cex:
            seen_cex.add(exchange_id)
            cex_rows.append((exchange_name, pair, trust or "N/A"))

        # DEX (uniswap, sushiswap, etc.)
        dex_ids = {"uniswap_v3", "uniswap_v2", "sushiswap", "pancakeswap_v3",
                   "raydium", "orca", "curve", "balancer", "trader_joe"}
        if exchange_id in dex_ids and exchange_id not in seen_dex:
            seen_dex.add(exchange_id)
            dex_rows.append((exchange_name, pair, "Spot"))

    # Sort CEX by priority order
    priority_order = {k: i for i, k in enumerate(priority_cex)}
    cex_rows.sort(key=lambda r: priority_order.get(r[0].lower().replace(" ", "_"), 99))

    return cex_rows[:10], dex_rows[:5]  # limit rows


def generate_page_content(data, hl_assets):
    """Generate full wiki page markdown from CoinGecko coin detail JSON."""
    coin_id = data.get("id", "unknown")
    name = data.get("name", coin_id.title())
    symbol = data.get("symbol", "").upper()
    categories = data.get("categories", [])
    md = get_safe(data, "market_data") or {}
    cd = get_safe(data, "community_data") or {}
    dd = get_safe(data, "developer_data") or {}
    links = data.get("links", {}) or {}
    platforms = data.get("platforms", {}) or {}

    # --- Description ---
    desc_raw = get_safe(data, "description", "en") or ""
    desc_clean = strip_html(desc_raw)
    # Lead paragraph: first 2 sentences
    lead = desc_clean[:500]
    if ". " in lead[50:]:
        first_dot = lead.index(". ") + 2
        second_dot = lead.find(". ", first_dot)
        if second_dot > 0:
            lead = lead[:second_dot + 1]
        else:
            lead = lead[:first_dot - 1]

    if not lead:
        cat_str = ", ".join(c for c in (categories or []) if c) or "cryptocurrency"
        lead = f"a {cat_str} project."
        lead_is_custom = True
    else:
        lead_is_custom = False
        # Strip leading "CoinName is " prefix since we add our own "**Name** (SYM) is"
        lower_name = name.lower()
        lower_lead = lead.lower()
        if lower_lead.startswith(lower_name + " is "):
            lead = lead[len(name) + 4:]
        elif lower_lead.startswith(lower_name + " ("):
            # Handle "Bitcoin (BTC) is ..." pattern
            paren_end = lead.find(") is ")
            if paren_end > 0:
                lead = lead[paren_end + 5:]
            else:
                lead = lead[len(name):].lstrip(" -—–")
        elif lower_lead.startswith(lower_name):
            # Name at start but different verb: "Bitcoin enables..."
            lead = lead[len(name):].lstrip(" -—–")
        else:
            # Description doesn't start with coin name — use as-is but prepend connector
            lead_is_custom = True  # signal to use different sentence structure

    # Full overview (truncate at 2000 chars)
    overview = desc_clean[:2000]
    if len(desc_clean) > 2000:
        overview += "..."

    # --- Frontmatter values ---
    rank = get_safe(md, "market_cap_rank") or get_safe(data, "market_cap_rank")
    genesis = data.get("genesis_date")
    founded_year = int(genesis[:4]) if genesis else None
    website = ""
    homepages = links.get("homepage", [])
    for hp in homepages:
        if hp:
            website = hp
            break

    tags = map_tags(categories)
    related = build_related_links(data, hl_assets)
    hashing = data.get("hashing_algorithm") or None

    # --- Exchange listings ---
    tickers = data.get("tickers", [])
    cex_rows, dex_rows = extract_exchange_listings(tickers, symbol)

    # Check Hyperliquid
    hl_listed = symbol in hl_assets

    # --- Build page ---
    lines = []

    # Frontmatter
    tag_str = ", ".join(tags)
    related_str = ", ".join(f'"{r}"' for r in related)
    lines.append("---")
    lines.append(f'title: "{name}"')
    lines.append("type: entity")
    lines.append(f"created: {TODAY}")
    lines.append(f"updated: {TODAY}")
    lines.append("status: draft")
    lines.append(f"tags: [{tag_str}]")
    lines.append(f'aliases: ["{symbol}"]')
    lines.append("entity_type: protocol")
    if founded_year:
        lines.append(f"founded: {founded_year}")
    lines.append('headquarters: "Decentralized"')
    if website:
        lines.append(f'website: "{website}"')
    lines.append(f"related: [{related_str}]")
    lines.append("---")
    lines.append("")

    # Title & lead
    rank_str = f" It ranks **#{rank}** by market capitalization." if rank else ""
    lines.append(f"# {name}")
    lines.append("")
    if not lead:
        lines.append(f"**{name}** ({symbol}) is a cryptocurrency.{rank_str}")
    elif lead_is_custom and lead[0].isupper():
        # Description doesn't relate to name — separate sentences
        lines.append(f"**{name}** ({symbol}) is a cryptocurrency.{rank_str} {lead}")
    else:
        # Clean up lead: if it starts with a verb after name stripping, adjust
        lead_clean = lead.lstrip()
        if lead_clean and lead_clean[0].islower():
            # Check if it reads naturally with "is" (e.g. "the world's first...")
            # vs. needs different phrasing (e.g. "seeks to link..." -> just use directly)
            verb_starts = ("seeks", "aims", "provides", "enables", "offers", "uses",
                          "allows", "connects", "was", "has", "combines", "leverages",
                          "utilizes", "supports", "serves", "builds", "creates",
                          "delivers", "focuses", "operates", "powers", "works")
            first_word = lead_clean.split()[0] if lead_clean.split() else ""
            if first_word in verb_starts:
                lines.append(f"**{name}** ({symbol}) {lead_clean}{rank_str}")
            else:
                lines.append(f"**{name}** ({symbol}) is {lead_clean[0].lower()}{lead_clean[1:]}{rank_str}")
        else:
            lines.append(f"**{name}** ({symbol}) is a cryptocurrency.{rank_str} {lead}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Key Facts
    lines.append("## Key Facts")
    lines.append("")
    lines.append("| Field | Detail |")
    lines.append("|---|---|")
    lines.append(f"| **Ticker** | {symbol} |")
    if rank:
        lines.append(f"| **Market Cap Rank** | #{rank} |")
    lines.append(f"| **Market Cap** | {fmt_usd(get_safe(md, 'market_cap', 'usd'))} |")
    lines.append(f"| **Current Price** | {fmt_usd(get_safe(md, 'current_price', 'usd'))} |")
    if genesis:
        lines.append(f"| **Genesis Date** | {genesis} |")
    if hashing:
        lines.append(f"| **Hashing Algorithm** | {hashing} |")
    if categories:
        # Filter out ecosystem tags (noisy), keep meaningful categories
        meaningful = [c for c in categories if c and "Ecosystem" not in c
                      and "Index" not in c and "Portfolio" not in c]
        if not meaningful:
            meaningful = [c for c in categories if c]
        # Limit to 8 most relevant
        cat_display = ", ".join(meaningful[:8])
        if len(meaningful) > 8:
            cat_display += f" (+{len(meaningful) - 8} more)"
        lines.append(f"| **Categories** | {cat_display} |")
    if website:
        lines.append(f"| **Website** | [{website}]({website}) |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Overview
    if overview:
        lines.append("## Overview")
        lines.append("")
        lines.append(overview)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Tokenomics
    circ = get_safe(md, "circulating_supply")
    total = get_safe(md, "total_supply")
    max_s = get_safe(md, "max_supply")
    fdv = get_safe(md, "fully_diluted_valuation", "usd")
    mcap_fdv = get_safe(md, "market_cap_fdv_ratio")

    lines.append("## Tokenomics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| **Circulating Supply** | {fmt_num(circ)} {symbol} |")
    lines.append(f"| **Total Supply** | {fmt_num(total)} {symbol} |")
    lines.append(f"| **Max Supply** | {fmt_num(max_s) + ' ' + symbol if max_s else 'Unlimited'} |")
    lines.append(f"| **Fully Diluted Valuation** | {fmt_usd(fdv)} |")
    if mcap_fdv:
        lines.append(f"| **Market Cap / FDV Ratio** | {mcap_fdv:.2f} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Price History
    ath = get_safe(md, "ath", "usd")
    ath_date = get_safe(md, "ath_date", "usd")
    ath_pct = get_safe(md, "ath_change_percentage", "usd")
    atl = get_safe(md, "atl", "usd")
    atl_date = get_safe(md, "atl_date", "usd")
    atl_pct = get_safe(md, "atl_change_percentage", "usd")
    pct_24h = get_safe(md, "price_change_percentage_24h")
    pct_7d = get_safe(md, "price_change_percentage_7d")
    pct_30d = get_safe(md, "price_change_percentage_30d")
    pct_1y = get_safe(md, "price_change_percentage_1y")

    lines.append("## Price History")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| **All-Time High** | {fmt_usd(ath)} ({fmt_date(ath_date)}) |")
    lines.append(f"| **Current vs ATH** | {fmt_pct(ath_pct)} |")
    lines.append(f"| **All-Time Low** | {fmt_usd(atl)} ({fmt_date(atl_date)}) |")
    lines.append(f"| **Current vs ATL** | {fmt_pct(atl_pct)} |")
    lines.append(f"| **24h Change** | {fmt_pct(pct_24h)} |")
    lines.append(f"| **7d Change** | {fmt_pct(pct_7d)} |")
    lines.append(f"| **30d Change** | {fmt_pct(pct_30d)} |")
    lines.append(f"| **1y Change** | {fmt_pct(pct_1y)} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Platform & Chain Information
    platform_id = data.get("asset_platform_id")
    lines.append("## Platform & Chain Information")
    lines.append("")
    non_empty_plat = {k: v for k, v in platforms.items() if v}
    if not platform_id and not non_empty_plat:
        lines.append("**Native Chain:** Own blockchain (Layer 1)")
    elif platform_id:
        lines.append(f"**Native Chain:** {platform_id.replace('-', ' ').title()}")
    else:
        lines.append("**Native Chain:** Multiple chains (see contract addresses below)")
    lines.append("")

    # Contract addresses
    if non_empty_plat:
        lines.append("### Contract Addresses")
        lines.append("")
        lines.append("| Chain | Address |")
        lines.append("|---|---|")
        for chain, addr in non_empty_plat.items():
            chain_display = chain.replace("-", " ").title() if chain else "Unknown"
            lines.append(f"| {chain_display} | `{addr}` |")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Exchange Listings
    lines.append("## Exchange Listings")
    lines.append("")

    if cex_rows:
        lines.append("### Centralized Exchanges")
        lines.append("")
        lines.append("| Exchange | Pair | Trust Score |")
        lines.append("|---|---|---|")
        for name_ex, pair, trust in cex_rows:
            lines.append(f"| {name_ex} | {pair} | {trust} |")
        lines.append("")

    if dex_rows or hl_listed:
        lines.append("### Decentralized Exchanges")
        lines.append("")
        lines.append("| Exchange | Pair | Type |")
        lines.append("|---|---|---|")
        if hl_listed:
            lines.append(f"| [[hyperliquid\\|Hyperliquid]] | {symbol}-PERP | Perpetual |")
        for name_ex, pair, type_ex in dex_rows:
            lines.append(f"| {name_ex} | {pair} | {type_ex} |")
        lines.append("")

    if not cex_rows and not dex_rows and not hl_listed:
        lines.append("> *No major exchange listings found in CoinGecko data.*")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Social & Community
    twitter = links.get("twitter_screen_name", "")
    reddit = links.get("subreddit_url", "")
    telegram = links.get("telegram_channel_identifier", "")
    chat_urls = links.get("chat_url", [])
    discord = ""
    for url in (chat_urls or []):
        if url and "discord" in url.lower():
            discord = url
            break
    repos = links.get("repos_url", {})
    github_urls = repos.get("github", []) if repos else []
    whitepaper = links.get("whitepaper", "")

    reddit_subs = get_safe(cd, "reddit_subscribers")
    telegram_count = get_safe(cd, "telegram_channel_user_count")

    lines.append("## Social & Community")
    lines.append("")
    lines.append("| Platform | Link / Metric |")
    lines.append("|---|---|")
    if website:
        lines.append(f"| **Website** | [{website}]({website}) |")
    if twitter:
        lines.append(f"| **Twitter** | [@{twitter}](https://twitter.com/{twitter}) |")
    if reddit:
        sub_str = f" ({fmt_num(reddit_subs)} subscribers)" if reddit_subs else ""
        lines.append(f"| **Reddit** | [{reddit}]({reddit}){sub_str} |")
    if telegram:
        tg_str = f" ({fmt_num(telegram_count)} members)" if telegram_count else ""
        lines.append(f"| **Telegram** | [{telegram}](https://t.me/{telegram}){tg_str} |")
    if discord:
        lines.append(f"| **Discord** | [{discord}]({discord}) |")
    if github_urls:
        gh = github_urls[0]
        lines.append(f"| **GitHub** | [{gh}]({gh}) |")
    if whitepaper:
        lines.append(f"| **Whitepaper** | [{whitepaper}]({whitepaper}) |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Developer Activity
    stars = get_safe(dd, "stars")
    forks = get_safe(dd, "forks")
    commits_4w = get_safe(dd, "commit_count_4_weeks")
    prs_merged = get_safe(dd, "pull_requests_merged")
    pr_contributors = get_safe(dd, "pull_request_contributors")

    has_dev = any(v for v in [stars, forks, commits_4w, prs_merged] if v)
    if has_dev:
        lines.append("## Developer Activity")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|---|---|")
        if stars:
            lines.append(f"| **GitHub Stars** | {fmt_num(stars)} |")
        if forks:
            lines.append(f"| **GitHub Forks** | {fmt_num(forks)} |")
        if commits_4w:
            lines.append(f"| **Commits (4 weeks)** | {fmt_num(commits_4w)} |")
        if prs_merged:
            lines.append(f"| **Pull Requests Merged** | {fmt_num(prs_merged)} |")
        if pr_contributors:
            lines.append(f"| **Contributors** | {fmt_num(pr_contributors)} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Trading Characteristics
    vol = get_safe(md, "total_volume", "usd")
    high_24 = get_safe(md, "high_24h", "usd")
    low_24 = get_safe(md, "low_24h", "usd")
    sentiment_up = data.get("sentiment_votes_up_percentage")

    lines.append("## Trading Characteristics")
    lines.append("")
    lines.append("| Characteristic | Detail |")
    lines.append("|---|---|")
    lines.append(f"| **24h Volume** | {fmt_usd(vol)} |")
    if rank:
        lines.append(f"| **Market Cap Rank** | #{rank} |")
    if high_24 and low_24:
        lines.append(f"| **24h Range** | {fmt_usd(low_24)} — {fmt_usd(high_24)} |")
    if sentiment_up is not None:
        lines.append(f"| **CoinGecko Sentiment** | {sentiment_up:.0f}% positive |")
    last_updated = data.get("last_updated")
    if last_updated:
        lines.append(f"| **Last Updated** | {fmt_date(last_updated)} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Whale & Holder Information
    lines.append("## Whale & Holder Information")
    lines.append("")
    lines.append("> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Major News & Events
    lines.append("## Major News & Events")
    lines.append("")
    lines.append("> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # See Also
    lines.append("## See Also")
    lines.append("")
    for link in related:
        lines.append(f"- {link}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sources
    lines.append("## Sources")
    lines.append("")
    lines.append(f"- (Source: [[{SOURCE_ID}]])")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Merge logic
# ---------------------------------------------------------------------------

def merge_page(existing_content, generated_content):
    """Merge generated content into existing page.

    - For good/excellent pages: only add missing sections
    - For stub/draft: enrich thin sections + add missing
    """
    ex_fm, ex_body = parse_frontmatter(existing_content)
    gen_fm, gen_body = parse_frontmatter(generated_content)

    status = get_status(ex_fm)
    is_high_quality = status in ("good", "excellent")

    ex_sections = parse_sections(ex_body)
    gen_sections = parse_sections(gen_body)

    # --- Merge frontmatter ---
    merged_fm = dict(ex_fm)
    for key, val in gen_fm.items():
        if key not in merged_fm or not merged_fm[key]:
            merged_fm[key] = val
        elif key == "related":
            # Merge related lists
            existing_related = merged_fm[key]
            new_related = val
            # Simple string concat approach for list values
            if new_related not in existing_related:
                # Parse both as lists and merge
                ex_items = set(re.findall(r'"(\[\[[^\]]+\]\])"', existing_related))
                gen_items = set(re.findall(r'"(\[\[[^\]]+\]\])"', new_related))
                all_items = ex_items | gen_items
                if all_items:
                    merged_fm[key] = "[" + ", ".join(f'"{i}"' for i in sorted(all_items)) + "]"
        elif key == "tags":
            # Merge tag lists
            ex_tags = set(re.findall(r'[\w-]+', merged_fm[key]))
            gen_tags = set(re.findall(r'[\w-]+', val))
            all_tags = ex_tags | gen_tags
            merged_fm[key] = "[" + ", ".join(sorted(all_tags)) + "]"
        elif key == "aliases":
            ex_aliases = set(re.findall(r'"([^"]+)"', merged_fm[key]))
            gen_aliases = set(re.findall(r'"([^"]+)"', val))
            all_aliases = ex_aliases | gen_aliases
            if all_aliases:
                merged_fm[key] = "[" + ", ".join(f'"{a}"' for a in sorted(all_aliases)) + "]"

    # Update the updated date
    merged_fm["updated"] = TODAY

    # --- Merge sections ---
    # Start with existing sections
    merged_sections = dict(ex_sections)

    for heading, content in gen_sections.items():
        if heading == "__lead__":
            continue  # never replace the lead paragraph

        if heading not in merged_sections:
            # Section doesn't exist — add it
            merged_sections[heading] = content
        elif not is_high_quality and len(merged_sections[heading].strip()) < 50:
            # Section exists but is very thin on a draft/stub — enrich it
            merged_sections[heading] = content

    # --- Reassemble page ---
    lines = ["---"]
    for key, val in merged_fm.items():
        if val is None:
            continue
        if isinstance(val, str) and not val.startswith("["):
            # Check if it needs quoting
            if key in ("title", "headquarters", "website"):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")

    # Lead
    if "__lead__" in merged_sections:
        lines.append(merged_sections["__lead__"])
        lines.append("")

    # All other sections in order: existing first, then new
    existing_headings = [h for h in ex_sections if h != "__lead__"]
    new_headings = [h for h in merged_sections if h not in ex_sections and h != "__lead__"]

    for heading in existing_headings + new_headings:
        if heading in merged_sections:
            content = merged_sections[heading]
            lines.append(f"## {heading}")
            lines.append("")
            lines.append(content)
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Existing page scanner
# ---------------------------------------------------------------------------

def scan_existing_pages():
    """Scan wiki/markets/crypto/ and return dict of {filename_stem: (path, status)}."""
    existing = {}
    for f in WIKI_CRYPTO.glob("*.md"):
        stem = f.stem
        if stem in NON_COIN_FILES:
            continue
        content = f.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_frontmatter(content)
        existing[stem] = (f, get_status(fm), content)
    return existing


def build_filename_map(coin_list, existing_pages):
    """Map CoinGecko IDs to wiki filenames, detecting overlaps."""
    # Build lookup indexes from existing pages
    existing_by_alias = {}
    existing_by_symbol_lower = {}
    for stem, (path, status, content) in existing_pages.items():
        fm, _ = parse_frontmatter(content)
        aliases_str = fm.get("aliases", "")
        for alias in re.findall(r'"([^"]+)"', aliases_str):
            existing_by_alias[alias.upper()] = stem
        # Also index by stem (which is often the symbol in lowercase)
        existing_by_symbol_lower[stem.upper()] = stem

    mapping = {}
    for coin in coin_list:
        cg_id = coin["id"]
        symbol = coin.get("symbol", "").upper()

        # Direct match: CG id matches existing filename
        if cg_id in existing_pages:
            mapping[cg_id] = cg_id
        # Symbol matches existing filename (e.g. xrp.md for CG id "ripple")
        elif symbol in existing_by_symbol_lower:
            mapping[cg_id] = existing_by_symbol_lower[symbol]
        # Alias match (e.g., existing page has aliases: ["XRP"])
        elif symbol in existing_by_alias:
            mapping[cg_id] = existing_by_alias[symbol]
        else:
            # Use CG id as filename (default)
            mapping[cg_id] = cg_id

    return mapping


# ---------------------------------------------------------------------------
# Source summary + index updates
# ---------------------------------------------------------------------------

def create_source_summary(coin_count, created_count, merged_count, skipped_count):
    """Create wiki/sources/coingecko-top-1000-YYYY-MM-DD.md"""
    content = f"""---
title: "CoinGecko Top 1000 Cryptocurrencies Data Import"
type: source
created: {TODAY}
updated: {TODAY}
status: good
tags: [crypto, data-provider, meta]
source_type: data
source_url: "https://api.coingecko.com/api/v3/"
source_author: "CoinGecko"
source_date: {TODAY}
source_file: "r2://trader-wiki/data/crypto-coins/"
confidence: high
claims_count: {coin_count}
---

# CoinGecko Top 1000 Cryptocurrencies Data Import

Batch import of the top {coin_count} cryptocurrencies by market capitalization from the CoinGecko API, supplemented with Hyperliquid exchange listing data from the CryptoData API.

## Data Points Extracted

- Coin metadata: name, symbol, description, categories, genesis date
- Market data: price, market cap, rank, volume, ATH/ATL, price changes
- Tokenomics: circulating supply, total supply, max supply, FDV
- Platform info: native chain, contract addresses across chains
- Exchange listings: CEX and DEX tickers with trust scores
- Social links: website, Twitter, Reddit, Telegram, Discord, GitHub
- Developer activity: GitHub stars, forks, commits, PRs, contributors
- Community metrics: Reddit subscribers, Telegram members
- Hyperliquid perpetual futures availability (cross-referenced from CryptoData API)
- CoinGecko sentiment data

## Import Statistics

| Metric | Count |
|---|---|
| **Total coins processed** | {coin_count} |
| **Pages created (new)** | {created_count} |
| **Pages merged (existing)** | {merged_count} |
| **Pages skipped** | {skipped_count} |
| **Data source** | CoinGecko API v3 |
| **Supplementary source** | CryptoData API (Hyperliquid listings) |
| **Confidence** | HIGH — official API data |
| **Import date** | {TODAY} |

## Methodology

1. Fetched top 1000 coins by market cap from `/coins/markets` endpoint
2. Fetched detailed data for each coin from `/coins/{{id}}` endpoint
3. Cross-referenced Hyperliquid perpetual futures listings from CryptoData API
4. Generated wiki pages following the entity template with all available data
5. Merged new data into existing pages without overwriting hand-written content

## Limitations

- Price data is a point-in-time snapshot (as of {TODAY}), not live
- Whale/holder information not available from these APIs — requires on-chain analytics
- News events not available from these APIs — to be added via wiki ingestion workflow
- Some coins may have incomplete data (missing descriptions, no social links, etc.)
- CoinGecko descriptions may contain marketing language — treat as informational, not editorial
"""
    path = WIKI_SOURCES / f"{SOURCE_ID}.md"
    path.write_text(content, encoding="utf-8")
    return path


def append_log_entry(coin_count, created_pages, merged_pages):
    """Append entry to wiki/log.md."""
    log_path = WIKI_ROOT / "log.md"
    if not log_path.exists():
        log_path.write_text("# Wiki Log\n\n", encoding="utf-8")

    created_links = ", ".join(f"[[{p}]]" for p in created_pages[:20])
    if len(created_pages) > 20:
        created_links += f" ... and {len(created_pages) - 20} more"

    merged_links = ", ".join(f"[[{p}]]" for p in merged_pages[:10])
    if len(merged_pages) > 10:
        merged_links += f" ... and {len(merged_pages) - 10} more"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    entry = f"""
## {timestamp} — Batch Import: Top {coin_count} Cryptocurrencies (CoinGecko)

- Source: [[{SOURCE_ID}]]
- Type: data (API batch import)
- Pages created ({len(created_pages)}): {created_links}
- Pages merged ({len(merged_pages)}): {merged_links}
- Data points per coin: 20 (metadata, market data, tokenomics, social, developer, exchange listings)
- Confidence: HIGH (official CoinGecko API data)
"""

    existing = log_path.read_text(encoding="utf-8")
    # Insert after the first heading
    if "\n## " in existing:
        # Insert before the first log entry
        idx = existing.index("\n## ") + 1
        updated = existing[:idx] + entry + "\n" + existing[idx:]
    else:
        updated = existing + entry

    log_path.write_text(updated, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("Crypto Wiki Page Generator")
    print(f"Data dir: {DATA_DIR}")
    print(f"Output dir: {WIKI_CRYPTO}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("=" * 60)

    # Load coin list
    coin_list_file = DATA_DIR / "_coin_list.json"
    if not coin_list_file.exists():
        print("ERROR: No coin list found. Run fetch_crypto_coins.py first.")
        sys.exit(1)

    coin_list = json.loads(coin_list_file.read_text(encoding="utf-8"))
    print(f"Loaded {len(coin_list)} coins from list")

    # Load Hyperliquid data
    hl_assets = load_hyperliquid_assets()
    print(f"Loaded {len(hl_assets)} Hyperliquid assets")

    # Scan existing pages
    existing_pages = scan_existing_pages()
    print(f"Found {len(existing_pages)} existing crypto coin pages")

    # Build filename mapping
    filename_map = build_filename_map(coin_list, existing_pages)

    # Process each coin
    created_pages = []
    merged_pages = []
    skipped_pages = []
    scope_skipped = []
    error_pages = []

    for i, coin in enumerate(coin_list, 1):
        cg_id = coin["id"]
        symbol = coin.get("symbol", "?").upper()
        rank = coin.get("market_cap_rank", "?")

        # Load detail JSON
        detail_file = DATA_DIR / f"{cg_id}.json"
        if not detail_file.exists():
            if i % 100 == 0:
                print(f"  [{i}/{len(coin_list)}] Skipping {symbol} — no detail data")
            skipped_pages.append(cg_id)
            continue

        data = json.loads(detail_file.read_text(encoding="utf-8"))

        # Scope filter: skip tokenized single-name equities / equity ETFs (repo: no equity content)
        if is_out_of_scope_equity(cg_id, data.get("name", ""), data.get("categories", [])):
            scope_skipped.append(cg_id)
            continue

        # Determine target filename
        wiki_filename = filename_map.get(cg_id, cg_id)
        target_path = WIKI_CRYPTO / f"{wiki_filename}.md"

        # Generate page content
        generated = generate_page_content(data, hl_assets)

        if wiki_filename in existing_pages:
            # Merge into existing
            _, status, existing_content = existing_pages[wiki_filename]
            merged = merge_page(existing_content, generated)
            if not dry_run:
                target_path.write_text(merged, encoding="utf-8")
            merged_pages.append(wiki_filename)
            if i % 50 == 0 or i <= 5:
                print(f"  [{i}/{len(coin_list)}] #{rank} {symbol} — MERGED into {wiki_filename}.md (status: {status})")
        else:
            # Create new
            if not dry_run:
                target_path.write_text(generated, encoding="utf-8")
            created_pages.append(wiki_filename)
            if i % 50 == 0 or i <= 5:
                print(f"  [{i}/{len(coin_list)}] #{rank} {symbol} — CREATED {wiki_filename}.md")

    print(f"\n{'=' * 60}")
    print(f"Results:")
    print(f"  Created: {len(created_pages)}")
    print(f"  Merged:  {len(merged_pages)}")
    print(f"  Skipped: {len(skipped_pages)} (no detail data)")
    print(f"  Scope-skipped: {len(scope_skipped)} (tokenized single-name equities/ETFs)")
    print(f"  Errors:  {len(error_pages)}")
    print(f"{'=' * 60}")

    if dry_run:
        print("\nDRY RUN — no files were written.")
        return

    # Create source summary
    total_processed = len(created_pages) + len(merged_pages)
    src_path = create_source_summary(total_processed, len(created_pages), len(merged_pages), len(skipped_pages))
    print(f"\nSource summary: {src_path}")

    # Append log entry
    append_log_entry(total_processed, created_pages, merged_pages)
    print("Log entry appended to wiki/log.md")

    print(f"\nDone! {total_processed} pages processed.")
    print(f"Next: python tools/lint.py")


if __name__ == "__main__":
    main()
