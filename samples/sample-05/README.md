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

---

## Optional — automate it with code (advanced)
You do **not** need this for the course. The included **`main.py`** is the worked reference
script: a command-line **API Fetch & Save** tool that does the same job on your own computer.
It fetches JSON from a URL and appends it, timestamped, to a local file. With `--interval` it
keeps polling. It uses only the Python standard library — no API key for the default public
test API.

### Run it

```bash
# Fetch the default public API once (JSONPlaceholder)
python main.py

# Fetch a custom URL
python main.py --url https://jsonplaceholder.typicode.com/posts/1

# Save to a specific file
python main.py --url https://jsonplaceholder.typicode.com/users/1 --output users.json

# Poll every 30 seconds (Ctrl+C to stop)
python main.py --url https://jsonplaceholder.typicode.com/todos/1 --interval 30
```

### Expected output (single fetch)

```
Fetching: https://jsonplaceholder.typicode.com/todos/1

[#1] Fetched at : 2024-01-15T10:30:45.123456+00:00
  URL      : https://jsonplaceholder.typicode.com/todos/1
  Status   : 200
  userId   : 1
  id       : 1
  title    : delectus aut autem
  completed: False

[Saved] data.json  (1 record(s) total)
```

### Output file format

Records are saved as a JSON array, with each entry timestamped:

```json
[
  {
    "fetched_at": "2024-01-15T10:30:45.123456+00:00",
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "status": 200,
    "data": {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": false
    }
  }
]
```

### Notes
- If the output file already exists, new records are **appended** (not overwritten).
- Works with any public JSON API — no API key required for the default URL.
- The `--timeout` flag (default: 10s) controls the request timeout.
- Errors during polling are logged and the script continues retrying.
