# HO13 Sample 4 — Turn a CSV into a Weekly Report

## What you'll build
A report generator. Every week you probably stare at the same kind of spreadsheet and
hand-write a summary. Instead, you upload the CSV and Claude writes the report for you —
totals, top performers, and a short readable narrative you can paste straight into an email.
No coding.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Pro or Team, which includes **Cowork**).

1. Open **Claude.ai** and start a **Cowork** session (the workspace where you can drop files).
2. Drag in the sample file from this folder's **`sample_data/`** (`sales.csv`) — or your own
   weekly export.
3. Copy **the example prompt** below and paste it into the chat.
4. Claude reads the data and writes you a formatted summary report you can download or copy.

## The example prompt
Copy this exactly into Cowork after uploading your CSV:

```
I've uploaded a sales CSV. Please write me a clean weekly summary report from it.

Include these sections:
1. Overview — how many rows, the date range covered, and the grand total of sales.
2. Top performers — the top 5 by total sales (e.g. top regions or products), as a table.
3. Key numbers — total, average, highest single sale, and lowest single sale.
4. A short narrative — 3 or 4 plain-English sentences I could paste into an email,
   highlighting what stood out this week.

Give me the report as a downloadable Markdown file, and also show it in the chat.
Only use the data in the file — don't invent any numbers.
```

## Make it your own
- Point it at your own weekly export (sales, signups, support tickets — anything).
- Ask for the narrative in your brand's tone, or in a different language.
- Ask Claude to add a simple bar chart of the top 5 to the report.

---

## Optional — automate it with code (advanced)
You do **not** need this for the course. The included **`main.py`** is the worked reference
script: a command-line **CSV Summary Report Generator** that does the same job on your own
computer. It computes row count and per-column stats (min/max/mean for numeric columns, top 5
values for text columns) and writes a formatted Markdown report. It uses only the Python
standard library — no API key, nothing to install.

### Run it

```bash
# Generate report with default filename (report_sales.md)
python main.py sample_data/sales.csv

# Specify output file
python main.py sample_data/sales.csv --output report.md
python main.py data.csv -o reports/summary.md
```

### Expected output (console)

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

### Generated Markdown report structure

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

### Notes
- A column is treated as numeric if 80%+ of non-empty values parse as numbers.
- Works on any CSV regardless of column names or count.
- Handles UTF-8 BOM (Excel exports) automatically.
