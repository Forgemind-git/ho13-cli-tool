"""
CSV Data Cleaner
Reads a CSV, deduplicates rows, strips whitespace from string columns,
standardises column names to snake_case, and reports fixes.
"""

import argparse
import csv
import re
import sys
from pathlib import Path


def to_snake_case(name):
    """Convert a column name to snake_case."""
    name = name.strip()
    # Replace spaces and hyphens with underscores
    name = re.sub(r"[\s\-]+", "_", name)
    # Insert underscore before capital letters (CamelCase -> camel_case)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)
    # Remove non-word chars except underscore
    name = re.sub(r"[^\w]", "", name)
    return name.lower().strip("_")


def clean_csv(input_path, output_path):
    """
    Clean the CSV file and write results to output_path.
    Returns a dict with stats about what was fixed.
    """
    stats = {
        "original_rows": 0,
        "duplicate_rows_removed": 0,
        "whitespace_cells_fixed": 0,
        "columns_renamed": 0,
        "original_columns": [],
        "clean_columns": [],
    }

    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    if input_path.suffix.lower() != ".csv":
        print(f"[WARN] File does not have a .csv extension: {input_path}")

    # Read file
    try:
        with open(input_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                print("[ERROR] CSV file is empty or has no header row.")
                sys.exit(1)

            original_columns = list(reader.fieldnames)
            stats["original_columns"] = original_columns
            rows = list(reader)
    except Exception as e:
        print(f"[ERROR] Could not read CSV: {e}")
        sys.exit(1)

    stats["original_rows"] = len(rows)
    print(f"\nLoaded {len(rows)} row(s) with {len(original_columns)} column(s) from: {input_path.name}")

    # --- Step 1: Standardise column names ---
    clean_columns = [to_snake_case(col) for col in original_columns]
    renamed = [(o, c) for o, c in zip(original_columns, clean_columns) if o != c]
    stats["columns_renamed"] = len(renamed)
    stats["clean_columns"] = clean_columns

    if renamed:
        print(f"\n[Step 1] Renaming {len(renamed)} column(s):")
        for old, new in renamed:
            print(f"  '{old}'  ->  '{new}'")
    else:
        print("\n[Step 1] Column names are already clean.")

    # Rename keys in rows
    col_map = dict(zip(original_columns, clean_columns))
    rows = [{col_map[k]: v for k, v in row.items()} for row in rows]

    # --- Step 2: Strip whitespace from string values ---
    whitespace_fixed = 0
    cleaned_rows = []
    for row in rows:
        new_row = {}
        for col, val in row.items():
            if isinstance(val, str) and val != val.strip():
                new_row[col] = val.strip()
                whitespace_fixed += 1
            else:
                new_row[col] = val
        cleaned_rows.append(new_row)
    rows = cleaned_rows
    stats["whitespace_cells_fixed"] = whitespace_fixed

    if whitespace_fixed:
        print(f"\n[Step 2] Stripped whitespace from {whitespace_fixed} cell(s).")
    else:
        print("\n[Step 2] No leading/trailing whitespace found.")

    # --- Step 3: Deduplicate rows ---
    seen = set()
    unique_rows = []
    for row in rows:
        key = tuple(row[c] for c in clean_columns)
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)

    duplicates_removed = len(rows) - len(unique_rows)
    stats["duplicate_rows_removed"] = duplicates_removed

    if duplicates_removed:
        print(f"\n[Step 3] Removed {duplicates_removed} duplicate row(s).")
    else:
        print("\n[Step 3] No duplicate rows found.")

    rows = unique_rows

    # --- Write output ---
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=clean_columns)
            writer.writeheader()
            writer.writerows(rows)
        print(f"\n[Done] Cleaned CSV written to: {output_path}")
    except Exception as e:
        print(f"[ERROR] Could not write output: {e}")
        sys.exit(1)

    return stats, len(rows)


def print_summary(stats, final_row_count):
    print(f"\n{'='*50}")
    print("  CLEANING SUMMARY")
    print(f"{'='*50}")
    print(f"  Original rows      : {stats['original_rows']}")
    print(f"  Duplicates removed : {stats['duplicate_rows_removed']}")
    print(f"  Final rows         : {final_row_count}")
    print(f"  Columns renamed    : {stats['columns_renamed']}")
    print(f"  Whitespace fixes   : {stats['whitespace_cells_fixed']}")
    print(f"\n  Columns: {', '.join(stats['clean_columns'])}")
    print(f"{'='*50}\n")


def main():
    parser = argparse.ArgumentParser(
        prog="csv-cleaner",
        description=(
            "CSV Data Cleaner — deduplicates rows, strips whitespace, "
            "standardises column names to snake_case, and reports what was fixed."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py sample_data/messy.csv
  python main.py sample_data/messy.csv --output clean.csv
  python main.py data.csv --output data/cleaned.csv
        """,
    )
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument(
        "--output", "-o", default=None,
        help="Path for cleaned output CSV (default: clean_<input_name>.csv)"
    )

    args = parser.parse_args()
    input_path = Path(args.input_csv)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.parent / f"clean_{input_path.name}"

    stats, final_row_count = clean_csv(input_path, output_path)
    print_summary(stats, final_row_count)


if __name__ == "__main__":
    main()
