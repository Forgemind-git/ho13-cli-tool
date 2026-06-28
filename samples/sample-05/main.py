"""
API Fetch & Save Script — Starter Skeleton
TODO: Replace this skeleton with the script Claude generates for you in Cowork.

Steps:
1. Fill in cowork-prompt.md with your Cowork prompt
2. (Optional) Upload API docs or a sample JSON response to Claude Cowork
3. Claude will generate a complete Python script
4. Paste the generated script here, replacing this file
"""

import argparse
import json
import sys
from pathlib import Path

# TODO: Set your API URL here (or accept it as a CLI argument)
DEFAULT_URL = "https://TODO_your_api_url_here"


def fetch_data(url, headers=None):
    """TODO: Fetch JSON data from the given URL.

    - Use urllib.request (stdlib, no pip needed) or requests if available
    - Return the parsed JSON as a dict/list
    - Handle HTTP errors gracefully
    """
    raise NotImplementedError("TODO: implement fetch_data()")


def extract_fields(data):
    """TODO: Pull out the fields you care about from the raw API response.

    - Navigate the JSON structure to find your target data
    - Return a flat list of dicts (one per record)
    """
    raise NotImplementedError("TODO: implement extract_fields()")


def save_data(records, output_path, fmt="json"):
    """TODO: Save the records to a file.

    - fmt="json"  → write JSON
    - fmt="csv"   → write CSV
    - fmt="md"    → write Markdown table
    - Timestamp the filename so each run doesn't overwrite the last
    """
    raise NotImplementedError("TODO: implement save_data()")


def main():
    parser = argparse.ArgumentParser(description="API Fetch & Save Script")
    parser.add_argument(
        "--url", default=DEFAULT_URL,
        help="API endpoint URL"
    )
    parser.add_argument(
        "--format", choices=["json", "csv", "md"], default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--output", default=".",
        help="Output directory (default: current directory)"
    )
    parser.add_argument(
        "--interval", type=int, default=0,
        help="Poll every N seconds (0 = run once)"
    )
    args = parser.parse_args()

    # TODO: Fetch, extract, save — and loop if --interval is set
    raw = fetch_data(args.url)
    records = extract_fields(raw)
    output_path = Path(args.output)
    save_data(records, output_path, fmt=args.format)


if __name__ == "__main__":
    main()
