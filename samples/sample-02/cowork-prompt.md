# Cowork Prompt: csv cleaner

## What to paste into Cowork

Upload the sample file first (`sample_data/messy.csv` — or your own messy CSV/Excel
export), then paste this:

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

---

**Example structure to adapt:**

> I have uploaded a messy CSV file with inconsistent formatting.
> Please clean it by:
> - Standardising all column names to snake_case
> - Removing duplicate rows
> - Stripping leading/trailing whitespace from all values
> - Flagging or filling missing values
> Then generate a Python script that performs these same steps automatically on any similar CSV.
> Show me a before/after row count and a list of columns that were renamed.
