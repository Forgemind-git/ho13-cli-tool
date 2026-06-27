# Sample 05 — API Fetch & Save Script

Fetches JSON from a URL, saves it timestamped to a local file. With `--interval`, keeps polling and appending. Shows the last fetched value on each run.

## Install

```bash
pip install -r requirements.txt
```

No external dependencies — stdlib only.

## Usage

```bash
# Fetch the default public API once (JSONPlaceholder)
python main.py

# Fetch a custom URL
python main.py --url https://jsonplaceholder.typicode.com/posts/1

# Save to a specific file
python main.py --url https://jsonplaceholder.typicode.com/users/1 --output users.json

# Poll every 30 seconds (Ctrl+C to stop)
python main.py --url https://jsonplaceholder.typicode.com/todos/1 --interval 30

# Poll a real-world public API for Bitcoin price
python main.py --url https://api.coindesk.com/v1/bpi/currentprice.json --interval 60 --output bitcoin.json
```

## Expected Output (single fetch)

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

## Expected Output (polling mode)

```
Polling: https://jsonplaceholder.typicode.com/todos/1
Interval: every 30s  |  Output: data.json
Press Ctrl+C to stop.

[10:30:45] Fetching (#1)...

[#1] Fetched at : 2024-01-15T10:30:45+00:00
  URL      : https://jsonplaceholder.typicode.com/todos/1
  Status   : 200
  ...
  -> data.json  (1 record(s) total)

Next fetch in 30s  (Ctrl+C to stop)
```

## Output File Format

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

## Notes

- If the output file already exists, new records are **appended** (not overwritten).
- Works with any public JSON API — no API key required for the default URL.
- The `--timeout` flag (default: 10s) controls the request timeout.
- Errors during polling are logged and the script continues retrying.
