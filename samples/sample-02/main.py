"""
CSV Data Cleaner — Starter Skeleton
TODO: Replace this skeleton with the script Claude generates for you in Cowork.

Steps:
1. Fill in cowork-prompt.md with your Cowork prompt
2. Upload your messy CSV to Claude Cowork
3. Claude will generate a complete Python script
4. Paste the generated script here, replacing this file
"""

import argparse
import csv
import sys
from pathlib import Path


def to_snake_case(name):
    """TODO: Convert a column name to snake_case."""
    # TODO: Strip whitespace, replace spaces/hyphens with underscores,
    # handle CamelCase, remove special characters
    raise NotImplementedError("TODO: implement to_snake_case()")


def clean_csv(input_path, output_path):
    """TODO: Read, clean, and write a CSV file.

    Cleaning steps to implement:
    - Standardise column names (snake_case)
    - Strip whitespace from all string values
    - Remove duplicate rows
    - Handle missing/empty values
    - Report how many rows and columns were fixed
    """
    raise NotImplementedError("TODO: implement clean_csv()")


def main():
    parser = argparse.ArgumentParser(description="CSV Data Cleaner")
    parser.add_argument("input", help="Path to the messy CSV file")
    parser.add_argument(
        "-o", "--output",
        help="Path for the cleaned CSV (default: input_cleaned.csv)"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_stem(input_path.stem + "_cleaned")

    # TODO: Call clean_csv and print a summary
    clean_csv(input_path, output_path)


if __name__ == "__main__":
    main()
