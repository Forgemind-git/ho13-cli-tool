# Cowork Prompt: fetch and save

## What to paste into Cowork

Optionally upload `sample_data/example_output.json` first (so Claude matches the exact
output shape), then paste this:

```
Please fetch some data from a public API and save it to a tidy file for me.

1. Fetch this URL (a free public test API, no key needed):
   https://jsonplaceholder.typicode.com/todos/1
2. Show me the main fields you got back (id, title, completed, etc.).
3. Save the result to a JSON file shaped like the example_output.json I uploaded:
   each record wrapped with a "fetched_at" timestamp, the source "url", the HTTP "status",
   and the raw "data".
4. Give me the file to download, and tell me how many records it contains.
```

---

**Example structure to adapt:**

> I need a Python script to fetch data from this API: [TODO: your URL]
> The API returns JSON with this structure: [TODO: paste a sample response or describe it]
> I want to extract: [TODO: list the fields you need, e.g. id, name, created_at, status]
> Save the results as [TODO: CSV / JSON / Markdown] with a timestamp in the filename.
> Use only Python standard library (no pip install needed).
> Optionally, add a --interval flag to poll every N seconds and append new data.
