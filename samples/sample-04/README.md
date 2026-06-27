# Sample 04 — CSV Summary Report Generator

Reads a CSV, computes row count, column stats (min/max/mean for numeric columns, top 5 values for text columns), and writes a formatted markdown report. Works on any CSV.

## Install

```bash
pip install -r requirements.txt
```

No external dependencies — stdlib only.

## Usage

```bash
# Generate report with default filename (report_sales.md)
python main.py sample_data/sales.csv

# Specify output file
python main.py sample_data/sales.csv --output report.md
python main.py data.csv -o reports/summary.md
```

## Expected Output (console)

```
Analysing: sales.csv
  200 row(s) x 6 column(s)

[Done] Report written to: report_sales.md

=============================================
  REPORT SUMMARY
=============================================
  Rows analysed    : 200
  Total columns    : 6
  Numeric columns  : 3
  Text columns     : 3
  Output           : report_sales.md
=============================================
```

## Generated Markdown Report Structure

```markdown
# CSV Summary Report: `sales.csv`

## Overview
| Property | Value |
...

## Numeric Columns (3)
| Column | Count | Min | Max | Mean | Median | Sum | Empty |
...

## Text Columns (3)
### `region`
- Count: 200
- Unique values: 4
- Top 5 values:
  | Value | Count |
  | North | 55    |
  ...
```

## Notes

- A column is treated as numeric if 80%+ of non-empty values parse as numbers.
- Works on any CSV regardless of column names or count.
- Handles UTF-8 BOM (Excel exports) automatically.
