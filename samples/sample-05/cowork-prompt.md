# Cowork Prompt: fetch and save

## What to paste into Cowork

[TODO: Write your Cowork prompt here.

Your prompt should tell Claude:
1. What the uploaded files contain
2. What processing to apply
3. What the output should look like (format, columns, sections)

Be specific — Claude works best with clear instructions.]

---

**Example structure to adapt:**

> I need a Python script to fetch data from this API: [TODO: your URL]
> The API returns JSON with this structure: [TODO: paste a sample response or describe it]
> I want to extract: [TODO: list the fields you need, e.g. id, name, created_at, status]
> Save the results as [TODO: CSV / JSON / Markdown] with a timestamp in the filename.
> Use only Python standard library (no pip install needed).
> Optionally, add a --interval flag to poll every N seconds and append new data.
