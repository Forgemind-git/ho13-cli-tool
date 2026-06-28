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

## Optional — automate it with code (advanced)
You do **not** need this for the course. If you later want to clean files on your own
computer, **`main.py`** in this folder is a ready-to-run Python script that does the same
job. It uses only the Python standard library — no API key, nothing to install. Run
`python main.py sample_data/messy.csv` and it writes a cleaned copy next to the original.
