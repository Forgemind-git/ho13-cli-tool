"""
CSV Summary Report Generator
Reads a CSV, computes column statistics, and writes a formatted markdown report.
"""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


def try_float(val):
    """Try to convert a value to float; return None on failure."""
    try:
        return float(val.strip())
    except (ValueError, AttributeError):
        return None


def analyse_column(values):
    """
    Analyse a column's values.
    Returns a dict with type ('numeric' or 'text') and stats.
    """
    non_empty = [v for v in values if v is not None and str(v).strip() != ""]
    empty_count = len(values) - len(non_empty)

    if not non_empty:
        return {"type": "empty", "empty": len(values)}

    # Try numeric
    numeric_vals = [try_float(v) for v in non_empty]
    numeric_vals_clean = [v for v in numeric_vals if v is not None]

    if len(numeric_vals_clean) >= len(non_empty) * 0.8:
        # Treat as numeric
        n = len(numeric_vals_clean)
        total = sum(numeric_vals_clean)
        mean = total / n
        sorted_vals = sorted(numeric_vals_clean)
        mid = n // 2
        median = (sorted_vals[mid] + sorted_vals[~mid]) / 2
        return {
            "type": "numeric",
            "count": n,
            "empty": empty_count,
            "min": sorted_vals[0],
            "max": sorted_vals[-1],
            "mean": mean,
            "median": median,
            "sum": total,
        }
    else:
        # Text column
        counter = Counter(str(v).strip() for v in non_empty)
        top5 = counter.most_common(5)
        unique = len(counter)
        return {
            "type": "text",
            "count": len(non_empty),
            "empty": empty_count,
            "unique": unique,
            "top5": top5,
        }


def generate_report(input_path, output_path):
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print("[ERROR] CSV has no header row.")
                sys.exit(1)
            columns = list(reader.fieldnames)
            rows = list(reader)
    except Exception as e:
        print(f"[ERROR] Could not read CSV: {e}")
        sys.exit(1)

    row_count = len(rows)
    col_count = len(columns)
    print(f"\nAnalysing: {input_path.name}")
    print(f"  {row_count} row(s) x {col_count} column(s)\n")

    # Analyse each column
    col_analyses = {}
    for col in columns:
        values = [row.get(col, "") for row in rows]
        col_analyses[col] = analyse_column(values)

    # Build markdown report
    lines = []
    lines.append(f"# CSV Summary Report: `{input_path.name}`\n")
    lines.append(f"Generated from file: `{input_path}`\n")
    lines.append(f"## Overview\n")
    lines.append(f"| Property | Value |")
    lines.append(f"|----------|-------|")
    lines.append(f"| File | `{input_path.name}` |")
    lines.append(f"| Rows | {row_count} |")
    lines.append(f"| Columns | {col_count} |")
    lines.append(f"| Column names | {', '.join(f'`{c}`' for c in columns)} |")
    lines.append(f"")

    # Numeric columns section
    numeric_cols = [(c, a) for c, a in col_analyses.items() if a["type"] == "numeric"]
    text_cols = [(c, a) for c, a in col_analyses.items() if a["type"] == "text"]
    empty_cols = [(c, a) for c, a in col_analyses.items() if a["type"] == "empty"]

    if numeric_cols:
        lines.append(f"## Numeric Columns ({len(numeric_cols)})\n")
        lines.append(f"| Column | Count | Min | Max | Mean | Median | Sum | Empty |")
        lines.append(f"|--------|-------|-----|-----|------|--------|-----|-------|")
        for col, a in numeric_cols:
            lines.append(
                f"| `{col}` | {a['count']} | {a['min']:g} | {a['max']:g} | "
                f"{a['mean']:.2f} | {a['median']:.2f} | {a['sum']:g} | {a['empty']} |"
            )
        lines.append("")

    if text_cols:
        lines.append(f"## Text Columns ({len(text_cols)})\n")
        for col, a in text_cols:
            lines.append(f"### `{col}`\n")
            lines.append(f"- **Count (non-empty):** {a['count']}")
            lines.append(f"- **Empty cells:** {a['empty']}")
            lines.append(f"- **Unique values:** {a['unique']}")
            if a["top5"]:
                lines.append(f"- **Top 5 values:**\n")
                lines.append(f"  | Value | Count |")
                lines.append(f"  |-------|-------|")
                for val, cnt in a["top5"]:
                    lines.append(f"  | `{val}` | {cnt} |")
            lines.append("")

    if empty_cols:
        lines.append(f"## Empty Columns ({len(empty_cols)})\n")
        for col, _ in empty_cols:
            lines.append(f"- `{col}` — all values are empty\n")

    report_text = "\n".join(lines)

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_text, encoding="utf-8")
        print(f"[Done] Report written to: {output_path}")
    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")
        sys.exit(1)

    return row_count, col_count, len(numeric_cols), len(text_cols)


def main():
    parser = argparse.ArgumentParser(
        prog="csv-report",
        description=(
            "CSV Summary Report Generator — reads any CSV and writes a formatted "
            "markdown report with row count, min/max/mean for numeric columns, "
            "and top-5 values for text columns."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py sample_data/sales.csv
  python main.py sample_data/sales.csv --output report.md
  python main.py data.csv --output reports/summary.md
        """,
    )
    parser.add_argument("data_csv", help="Path to the input CSV file")
    parser.add_argument(
        "--output", "-o", default=None,
        help="Output markdown file path (default: report_<input_name>.md)"
    )

    args = parser.parse_args()
    input_path = Path(args.data_csv)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.parent / f"report_{input_path.stem}.md"

    rows, cols, num_cols, txt_cols = generate_report(input_path, output_path)

    print(f"\n{'='*45}")
    print(f"  REPORT SUMMARY")
    print(f"{'='*45}")
    print(f"  Rows analysed    : {rows}")
    print(f"  Total columns    : {cols}")
    print(f"  Numeric columns  : {num_cols}")
    print(f"  Text columns     : {txt_cols}")
    print(f"  Output           : {output_path}")
    print(f"{'='*45}\n")


if __name__ == "__main__":
    main()
