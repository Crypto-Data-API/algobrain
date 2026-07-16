#!/usr/bin/env python3
"""
Fetch top 1000 cryptocurrencies from CoinGecko + Hyperliquid listings from CryptoData API.

Saves raw JSON to raw/data/crypto-coins/ for wiki page generation.
Resumable: skips coins already fetched. Rate-limited at 30 calls/min.

Usage:
    python tools/fetch_crypto_coins.py
    python tools/fetch_crypto_coins.py --resume   # skip already-fetched coins (default)
    python tools/fetch_crypto_coins.py --fresh     # re-fetch everything
"""

import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime

import requests
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

COINGECKO_KEY = os.getenv("COINGECKO_API_KEY", "")
CRYPTODATA_KEY = os.getenv("CRYPTODATA_API_KEY", "")

CG_BASE = "https://api.coingecko.com/api/v3"
CD_BASE = "https://cryptodataapi.com/api/v1"

OUT_DIR = ROOT / "raw" / "data" / "crypto-coins"
PROGRESS_FILE = OUT_DIR / "_progress.json"
COIN_LIST_FILE = OUT_DIR / "_coin_list.json"
HL_FILE = OUT_DIR / "_hyperliquid-assets.json"

RATE_LIMIT_SLEEP = 2.1  # seconds between CoinGecko calls (30/min limit)
MAX_RETRIES = 3
BACKOFF_BASE = 5  # seconds for retry backoff

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def cg_headers():
    h = {"accept": "application/json"}
    if COINGECKO_KEY:
        h["x-cg-demo-api-key"] = COINGECKO_KEY
    return h


def cd_headers():
    h = {"accept": "application/json"}
    if CRYPTODATA_KEY:
        h["X-API-Key"] = CRYPTODATA_KEY
    return h


def fetch_with_retry(url, headers, params=None, label=""):
    """Fetch URL with retry + exponential backoff on 429/5xx."""
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 429:
                wait = BACKOFF_BASE * (2 ** attempt)
                print(f"  Rate limited on {label}. Waiting {wait}s (attempt {attempt+1}/{MAX_RETRIES})")
                time.sleep(wait)
            elif resp.status_code >= 500:
                wait = BACKOFF_BASE * (2 ** attempt)
                print(f"  Server error {resp.status_code} on {label}. Waiting {wait}s (attempt {attempt+1}/{MAX_RETRIES})")
                time.sleep(wait)
            else:
                print(f"  ERROR {resp.status_code} on {label}: {resp.text[:200]}")
                return None
        except requests.exceptions.RequestException as e:
            wait = BACKOFF_BASE * (2 ** attempt)
            print(f"  Network error on {label}: {e}. Waiting {wait}s (attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(wait)
    print(f"  FAILED after {MAX_RETRIES} retries: {label}")
    return None


def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {"fetched_ids": [], "started_at": None, "last_updated": None}


def save_progress(progress):
    progress["last_updated"] = datetime.utcnow().isoformat()
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Step 1: Fetch top 1000 coin list from /coins/markets
# ---------------------------------------------------------------------------

def fetch_coin_list():
    """Fetch top 2500 coins by market cap. Returns list of coin summaries."""
    if COIN_LIST_FILE.exists():
        print("Coin list already cached. Loading from disk...")
        return json.loads(COIN_LIST_FILE.read_text(encoding="utf-8"))

    all_coins = []
    for page in range(1, 11):  # 10 pages of 250 = 2500
        print(f"Fetching coin list page {page}/10...")
        data = fetch_with_retry(
            f"{CG_BASE}/coins/markets",
            headers=cg_headers(),
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 250,
                "page": page,
                "sparkline": "false",
                "price_change_percentage": "1h,24h,7d,14d,30d,200d,1y",
            },
            label=f"coins/markets page {page}",
        )
        if data:
            all_coins.extend(data)
            print(f"  Got {len(data)} coins (total: {len(all_coins)})")
        else:
            print(f"  WARNING: Failed to fetch page {page}")
        time.sleep(RATE_LIMIT_SLEEP)

    COIN_LIST_FILE.write_text(json.dumps(all_coins, indent=2), encoding="utf-8")
    print(f"Saved {len(all_coins)} coins to {COIN_LIST_FILE}")
    return all_coins


# ---------------------------------------------------------------------------
# Step 2: Fetch Hyperliquid asset list from CryptoData API
# ---------------------------------------------------------------------------

def fetch_hyperliquid_assets():
    """Fetch all Hyperliquid-listed assets from CryptoData API."""
    if HL_FILE.exists():
        print("Hyperliquid assets already cached. Loading from disk...")
        return json.loads(HL_FILE.read_text(encoding="utf-8"))

    print("Fetching Hyperliquid asset list from CryptoData API...")
    data = fetch_with_retry(
        f"{CD_BASE}/daily/hyperliquid",
        headers=cd_headers(),
        label="CryptoData hyperliquid daily",
    )
    if data:
        HL_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        # Count assets depending on response structure
        if isinstance(data, dict):
            asset_count = len(data.get("data", data.get("assets", data)))
        elif isinstance(data, list):
            asset_count = len(data)
        else:
            asset_count = "unknown"
        print(f"  Saved Hyperliquid data ({asset_count} assets)")
    else:
        print("  WARNING: Failed to fetch Hyperliquid data. Continuing without it.")
        HL_FILE.write_text(json.dumps({}), encoding="utf-8")
    return data


# ---------------------------------------------------------------------------
# Step 3: Fetch detailed data for each coin
# ---------------------------------------------------------------------------

def fetch_coin_detail(coin_id):
    """Fetch detailed data for a single coin from /coins/{id}."""
    out_file = OUT_DIR / f"{coin_id}.json"
    if out_file.exists():
        return True  # already fetched

    data = fetch_with_retry(
        f"{CG_BASE}/coins/{coin_id}",
        headers=cg_headers(),
        params={
            "localization": "false",
            "tickers": "true",
            "market_data": "true",
            "community_data": "true",
            "developer_data": "true",
            "sparkline": "false",
        },
        label=f"coins/{coin_id}",
    )
    if data:
        out_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return True
    return False


def fetch_all_details(coin_list, fresh=False):
    """Fetch details for all coins with rate limiting and progress tracking."""
    progress = load_progress()
    if fresh:
        progress["fetched_ids"] = []

    fetched_set = set(progress["fetched_ids"])
    total = len(coin_list)
    remaining = [c for c in coin_list if c["id"] not in fetched_set]

    if not remaining:
        print(f"All {total} coins already fetched!")
        return

    if not progress["started_at"]:
        progress["started_at"] = datetime.utcnow().isoformat()

    print(f"\nFetching details for {len(remaining)} coins ({total - len(remaining)} already done)...")
    est_minutes = len(remaining) * RATE_LIMIT_SLEEP / 60
    print(f"Estimated time: ~{est_minutes:.0f} minutes\n")

    success_count = 0
    fail_count = 0

    for i, coin in enumerate(remaining, 1):
        coin_id = coin["id"]
        rank = coin.get("market_cap_rank", "?")
        symbol = coin.get("symbol", "?").upper()

        # Use ASCII-safe print to avoid Windows encoding errors
        safe_label = f"[{i}/{len(remaining)}] #{rank} {symbol} ({coin_id})"
        try:
            print(f"{safe_label}...", end=" ", flush=True)
        except UnicodeEncodeError:
            ascii_label = safe_label.encode("ascii", "replace").decode("ascii")
            print(f"{ascii_label}...", end=" ", flush=True)

        ok = fetch_coin_detail(coin_id)
        if ok:
            success_count += 1
            progress["fetched_ids"].append(coin_id)
            print("OK")
        else:
            fail_count += 1
            print("FAILED")

        # Save progress every 25 coins
        if i % 25 == 0:
            save_progress(progress)
            print(f"  --- Progress saved: {success_count} OK, {fail_count} failed ---")

        time.sleep(RATE_LIMIT_SLEEP)

    save_progress(progress)
    print(f"\nDone! {success_count} fetched, {fail_count} failed out of {len(remaining)} remaining.")
    print(f"Total fetched: {len(progress['fetched_ids'])}/{total}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    fresh = "--fresh" in sys.argv

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Crypto Coin Data Fetcher")
    print(f"Output: {OUT_DIR}")
    print(f"CoinGecko key: {'set' if COINGECKO_KEY else 'NOT SET'}")
    print(f"CryptoData key: {'set' if CRYPTODATA_KEY else 'NOT SET'}")
    print(f"Mode: {'fresh' if fresh else 'resume'}")
    print("=" * 60)

    # Step 1: Get the top 1000 list
    coin_list = fetch_coin_list()
    if not coin_list:
        print("ERROR: No coins fetched. Check API key and network.")
        sys.exit(1)

    # Step 2: Get Hyperliquid listings
    fetch_hyperliquid_assets()

    # Step 3: Fetch details for each coin
    fetch_all_details(coin_list, fresh=fresh)

    # Summary
    json_count = len(list(OUT_DIR.glob("*.json"))) - 3  # exclude _progress, _coin_list, _hyperliquid
    print(f"\n{'=' * 60}")
    print(f"Complete. {json_count} coin detail files in {OUT_DIR}")
    print(f"Next: python tools/generate_crypto_pages.py")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
