# HO13 Sample 5 — Fetch Data and Save It

## What you'll build
A "grab it and save it" helper. If you keep copying the same data from a public website or
API and pasting it into a file, let Claude do it: it fetches the latest data and saves it in
a tidy file (JSON, CSV, or a Markdown table) — ready to reuse. No coding.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Pro or Team, which includes **Cowork**).

1. Open **Claude.ai** and start a **Cowork** session (the workspace where you can drop files).
2. (Optional) Drag in **`sample_data/example_output.json`** from this folder so Claude can
   see the exact output shape you want.
3. Copy **the example prompt** below and paste it into the chat.
4. Claude fetches the data, shows you the key values, and gives you a saved file to download.

## The example prompt
Copy this exactly into Cowork (upload `example_output.json` first if you want the same shape):

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

## Make it your own
- Swap the URL for any public API you use (weather, currency rates, your own data feed).
- Ask for the output as CSV or a Markdown table instead of JSON.
- Ask Claude to fetch several URLs and combine them into one file.

## Optional — automate it with code (advanced)
You do **not** need this for the course. If you later want this to run on a schedule on your
own computer, **`main.py`** in this folder is a ready-to-run Python script that fetches a URL
and appends timestamped records to a file. It uses only the Python standard library — no API
key for the default public test API. Run `python main.py` to try it, or
`python main.py --url <your-url> --interval 60` to poll. See the comments inside `main.py`.
