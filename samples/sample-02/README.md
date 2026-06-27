# Sample 02 — CSV Data Cleaner

Reads a CSV, deduplicates rows, strips whitespace from string columns, standardises column names to snake_case, and reports how many rows and columns were fixed.

## Install

```bash
pip install -r requirements.txt
```

No external dependencies — stdlib only.

## Usage

```bash
# Clean with default output name (clean_messy.csv)
python main.py sample_data/messy.csv

# Specify output file
python main.py sample_data/messy.csv --output clean.csv
python main.py sample_data/messy.csv -o data/cleaned.csv
```

## Expected Output

```
Loaded 8 row(s) with 5 column(s) from: messy.csv

[Step 1] Renaming 3 column(s):
  'First Name'  ->  'first_name'
  'Last Name'   ->  'last_name'
  'Email Address'  ->  'email_address'

[Step 2] Stripped whitespace from 5 cell(s).

[Step 3] Removed 2 duplicate row(s).

[Done] Cleaned CSV written to: clean_messy.csv

==================================================
  CLEANING SUMMARY
==================================================
  Original rows      : 8
  Duplicates removed : 2
  Final rows         : 6
  Columns renamed    : 3
  Whitespace fixes   : 5

  Columns: first_name, last_name, email_address, age, city
==================================================
```

## What It Fixes

| Issue | How it's fixed |
|-------|---------------|
| Column names with spaces | Converted to `snake_case` |
| CamelCase column names | Converted to `snake_case` |
| Leading/trailing whitespace in cells | Stripped |
| Duplicate rows (exact match) | First occurrence kept |

## Notes

- The original file is never overwritten; a new file is always written.
- Works on any CSV regardless of column count or types.
- UTF-8 BOM (`utf-8-sig`) is handled automatically for Excel-exported CSVs.
