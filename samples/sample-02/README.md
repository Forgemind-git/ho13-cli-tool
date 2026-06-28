# HO13 Sample 2 — Clean Up a Messy Spreadsheet

## What you'll build
A clean-up helper for ugly CSV exports — the ones with duplicate rows, wonky column names
("First Name", "first_name", "FIRSTNAME") and stray spaces everywhere. You upload the messy
file, Claude hands back a tidy one plus a plain-English list of what it fixed. No coding.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Pro or Team, which includes **Cowork**).

1. Open **Claude.ai** and start a **Cowork** session (the workspace where you can drop files).
2. Drag in the sample file from this folder's **`sample_data/`** (`messy.csv`) — or your own
   messy CSV/Excel export.
3. Copy **the example prompt** below and paste it into the chat.
4. Claude cleans the file and gives you a tidy CSV to download, plus a summary of changes.

## The example prompt
Copy this exactly into Cowork after uploading your CSV:

```
I've uploaded a messy CSV file. Please clean it up and give me a tidy version I can download.

Do all of the following:
1. Standardise the column headers to lowercase snake_case (e.g. "First Name" -> first_name).
2. Trim leading and trailing spaces from every cell.
3. Remove exact duplicate rows, keeping the first one.
4. Leave empty cells blank — don't guess or invent values.

Then give me:
- The cleaned file as a downloadable CSV (don't overwrite my original).
- A short summary: how many rows were in the original, how many duplicates you removed,
  how many rows remain, and which column names you changed.
```

## Make it your own
- Upload a real export from your CRM, store, or accounting tool.
- Ask Claude to also split one column into two (e.g. "Full Name" into first/last).
- Ask it to flag rows with missing emails instead of deleting them.

---

## Optional — automate it with code (advanced)
You do **not** need this for the course. The included **`main.py`** is the worked reference
script: a command-line **CSV Data Cleaner** that does the same job on your own computer. It
deduplicates rows, strips whitespace, standardises column names to snake_case, and reports
how many rows and columns were fixed. It uses only the Python standard library — no API key,
nothing to install.

### Run it

```bash
# Clean with default output name (clean_messy.csv)
python main.py sample_data/messy.csv

# Specify output file
python main.py sample_data/messy.csv --output clean.csv
python main.py sample_data/messy.csv -o data/cleaned.csv
```

### Expected output

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

### What it fixes

| Issue | How it's fixed |
|-------|---------------|
| Column names with spaces | Converted to `snake_case` |
| CamelCase column names | Converted to `snake_case` |
| Leading/trailing whitespace in cells | Stripped |
| Duplicate rows (exact match) | First occurrence kept |

### Notes
- The original file is never overwritten; a new file is always written.
- Works on any CSV regardless of column count or types.
- UTF-8 BOM (`utf-8-sig`) is handled automatically for Excel-exported CSVs.
