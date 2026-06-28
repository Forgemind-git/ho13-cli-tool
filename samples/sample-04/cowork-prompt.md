# Cowork Prompt: csv report

## What to paste into Cowork

[TODO: Write your Cowork prompt here.

Your prompt should tell Claude:
1. What the uploaded files contain
2. What processing to apply
3. What the output should look like (format, columns, sections)

Be specific — Claude works best with clear instructions.]

---

**Example structure to adapt:**

> I have uploaded a weekly CSV export from [TODO: your system, e.g. our sales tool / CRM / spreadsheet].
> The columns are: [TODO: list your columns, e.g. date, product, quantity, revenue, region]
> Please generate a Python script that reads this CSV and produces a Markdown summary report with:
> - Total rows and date range
> - Totals for: [TODO: e.g. revenue, quantity]
> - Top 5 by: [TODO: e.g. product by revenue]
> - Any rows with missing values flagged
> The script should work on any CSV with the same structure.
