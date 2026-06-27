"""
API Fetch & Save Script
Fetches JSON from a URL, saves it timestamped to a local file.
With --interval, keeps polling and appending.
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_json(url, timeout=10):
    """Fetch JSON from a URL. Returns parsed dict or raises an error."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "api-fetch-cli/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw), response.status
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Connection error: {e.reason}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Response is not valid JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")


def make_record(url, data, status_code):
    """Wrap the fetched data in a timestamped record."""
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "url": url,
        "status": status_code,
        "data": data,
    }


def load_existing_records(output_path):
    """Load existing records from the output file, or return empty list."""
    if not output_path.exists():
        return []
    try:
        content = output_path.read_text(encoding="utf-8").strip()
        if not content:
            return []
        parsed = json.loads(content)
        if isinstance(parsed, list):
            return parsed
        # Single record in file — wrap in list
        return [parsed]
    except json.JSONDecodeError:
        print(f"[WARN] Existing file is not valid JSON; starting fresh: {output_path}")
        return []


def save_records(records, output_path):
    """Save records list as pretty-printed JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def print_record(record, index=None):
    """Print a human-readable summary of a fetched record."""
    tag = f"[#{index}] " if index is not None else ""
    print(f"\n{tag}Fetched at : {record['fetched_at']}")
    print(f"  URL      : {record['url']}")
    print(f"  Status   : {record['status']}")
    data = record["data"]
    if isinstance(data, dict):
        for k, v in list(data.items())[:5]:
            print(f"  {k:12s}: {v}")
        if len(data) > 5:
            print(f"  ... ({len(data) - 5} more field(s))")
    elif isinstance(data, list):
        print(f"  (list with {len(data)} item(s))")
        if data:
            print(f"  First item: {json.dumps(data[0])[:120]}")
    else:
        print(f"  value    : {str(data)[:120]}")


def run_once(url, output_path):
    """Fetch once, append to file, print result."""
    print(f"Fetching: {url}")
    try:
        data, status = fetch_json(url)
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    records = load_existing_records(output_path)
    record = make_record(url, data, status)
    records.append(record)
    save_records(records, output_path)

    print_record(record, index=len(records))
    print(f"\n[Saved] {output_path}  ({len(records)} record(s) total)")


def run_polling(url, output_path, interval):
    """Keep fetching every `interval` seconds until interrupted."""
    print(f"Polling: {url}")
    print(f"Interval: every {interval}s  |  Output: {output_path}")
    print("Press Ctrl+C to stop.\n")

    fetch_count = 0
    try:
        while True:
            fetch_count += 1
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching (#{fetch_count})...")
            try:
                data, status = fetch_json(url)
                records = load_existing_records(output_path)
                record = make_record(url, data, status)
                records.append(record)
                save_records(records, output_path)
                print_record(record, index=len(records))
                print(f"  -> {output_path}  ({len(records)} record(s) total)")
            except RuntimeError as e:
                print(f"  [ERROR] {e} — will retry in {interval}s")

            print(f"\nNext fetch in {interval}s  (Ctrl+C to stop)")
            time.sleep(interval)
    except KeyboardInterrupt:
        print(f"\n\nStopped after {fetch_count} fetch(es). Data saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        prog="fetch-and-save",
        description=(
            "API Fetch & Save — fetches JSON from a URL and saves it timestamped. "
            "With --interval, keeps polling and appending new records."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  # Fetch the default public API once
  python main.py

  # Fetch a custom URL and save to a file
  python main.py --url https://api.coindesk.com/v1/bpi/currentprice.json --output bitcoin.json

  # Poll every 30 seconds
  python main.py --url https://jsonplaceholder.typicode.com/posts/1 --interval 30

Default URL: {DEFAULT_URL}
        """,
    )
    parser.add_argument(
        "--url", "-u", default=DEFAULT_URL,
        help=f"API URL to fetch (default: {DEFAULT_URL})"
    )
    parser.add_argument(
        "--output", "-o", default="data.json",
        help="Output JSON file path (default: data.json)"
    )
    parser.add_argument(
        "--interval", "-i", type=int, default=None,
        help="Poll every N seconds (omit for a single fetch)"
    )
    parser.add_argument(
        "--timeout", "-t", type=int, default=10,
        help="Request timeout in seconds (default: 10)"
    )

    args = parser.parse_args()
    output_path = Path(args.output)

    if args.interval is not None and args.interval <= 0:
        print("[ERROR] --interval must be a positive integer.")
        sys.exit(1)

    if args.interval:
        run_polling(args.url, output_path, args.interval)
    else:
        run_once(args.url, output_path)


if __name__ == "__main__":
    main()
