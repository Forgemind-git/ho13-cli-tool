"""
CSV Summary Report Generator — Starter Skeleton
TODO: Replace this skeleton with the script Claude generates for you in Cowork.

Steps:
1. Fill in cowork-prompt.md with your Cowork prompt
2. Upload your weekly CSV to Claude Cowork
3. Claude will generate a complete Python script
4. Paste the generated script here, replacing this file
"""

import argparse
import csv
import sys
from pathlib import Path


def analyse_column(values):
    """TODO: Return statistics for a single column's values.

    For numeric columns: min, max, mean, count of missing
    For text columns: top 5 most frequent values, count of unique, count of missing
    """
    raise NotImplementedError("TODO: implement analyse_column()")


def generate_report(input_path, output_path):
    """TODO: Read a CSV and write a Markdown summary report.

    Report sections to include:
    - Overview: filename, row count, column count
    - Per-column statistics (use analyse_column for each)
    - Any anomalies or notes
    """
    raise NotImplementedError("TODO: implement generate_report()")


def main():
    parser = argparse.ArgumentParser(description="CSV Summary Report Generator")
    parser.add_argument("input", help="Path to the CSV file")
    parser.add_argument(
        "-o", "--output",
        help="Path for the Markdown report (default: input_report.md)"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_stem(input_path.stem + "_report").with_suffix(".md")

    # TODO: Call generate_report and print confirmation
    generate_report(input_path, output_path)
    print(f"Report written to: {output_path}")


if __name__ == "__main__":
    main()
