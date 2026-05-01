#!/usr/bin/env python3
"""
Fetch publication and citation statistics for Richard O'Shaughnessy from NASA ADS API,
then write a JSON file for consumption by the site.

Usage:
    python3 bin/ads_stats.py [--config _config.yml] [--output assets/json/ads_stats.json]

Requirements:
    pip install requests pyyaml
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime

# ── Config ─────────────────────────────────────────────────────────────────────
DEFAULT_CONFIG = "_config.yml"
DEFAULT_OUTPUT = "assets/json/ads_stats.json"
SINCE_YEAR = 2010

# ADS API token — set ADS_TOKEN in your environment, or hard-code below.
ADS_TOKEN = os.environ.get("ADS_TOKEN", "")

# ── Helpers ───────────────────────────────────────────────────────────────────
def load_config(config_path: str) -> dict:
    import yaml
    with open(config_path) as f:
        return yaml.safe_load(f)


def fetch_ads_json(query: str, token: str, rows: int = 200) -> dict:
    """Hit ADS API v1 /search/docs endpoint and return the raw JSON."""
    import requests
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    params = {
        "q": query,
        "fl": "bibcode,year,citation_count,author",
        "rows": rows,
        "sort": "citation_count desc",
    }
    resp = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/docs",
        headers=headers,
        params=params,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def compute_stats(resp_json: dict, since_year: int) -> dict:
    """Aggregate pub / citation counts by year from ADS response."""
    docs = resp_json.get("response", {}).get("docs", [])
    current_year = datetime.now().year

    # Count publications per year
    pub_counts = {}
    citation_counts = {}
    for doc in docs:
        yr = doc.get("year")
        if yr is None or yr < since_year:
            continue
        pub_counts[yr] = pub_counts.get(yr, 0) + 1
        citation_counts[yr] = citation_counts.get(yr, 0) + doc.get("citation_count", 0)

    # Fill in missing years with zeros
    years = list(range(since_year, current_year + 1))
    pub_series  = [pub_counts.get(y, 0) for y in years]
    cite_series = [citation_counts.get(y, 0) for y in years]

    total_pubs   = sum(pub_series)
    total_cites  = sum(cite_series)

    return {
        "updated": datetime.utcnow().isoformat() + "Z",
        "since_year": since_year,
        "years": years,
        "publications": pub_series,
        "citations": cite_series,
        "total_publications": total_pubs,
        "total_citations": total_cites,
        # Raw per-year detail for reference / debugging
        "_pub_counts": pub_counts,
        "_cite_counts": citation_counts,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch ADS citation stats for O'Shaughnessy")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(f"Config not found: {args.config} — using defaults", file=sys.stderr)
        author_query = 'author:"O\'Shaughnessy, R."'
    else:
        cfg = load_config(args.config)
        scholar = cfg.get("social", {}).get("google_scholar", "")
        last_name  = cfg.get("scholar", {}).get("last_name", ["O'Shaughnessy"])[0]
        first_name = cfg.get("scholar", {}).get("first_name", ["R"])[0]
        author_query = f'author:"{last_name}, {first_name}"'

    if not ADS_TOKEN:
        print("WARNING: ADS_TOKEN not set. API calls will be rate-limited or fail.", file=sys.stderr)
        print("  Export it:  export ADS_TOKEN='your-token-here'", file=sys.stderr)

    print(f"Query: {author_query}")
    resp = fetch_ads_json(author_query, ADS_TOKEN)
    stats = compute_stats(resp, SINCE_YEAR)

    print(f"  Total publications (since {SINCE_YEAR}): {stats['total_publications']}")
    print(f"  Total citations   (since {SINCE_YEAR}): {stats['total_citations']}")

    if args.dry_run:
        print(json.dumps(stats, indent=2))
        return

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
