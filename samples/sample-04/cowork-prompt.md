# Cowork Prompt: csv report

## What to paste into Cowork

Upload the sample file first (`sample_data/sales.csv` — or your own weekly export),
then paste this:

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
