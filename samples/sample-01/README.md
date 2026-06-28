# HO13 Sample 1 — Tidy a Messy Folder

## What you'll build
A little helper that takes a pile of random files (the kind that clog up your Downloads
folder) and sorts them into neat folders by type — Images, Documents, Videos, Code, and so
on. You hand Claude the files, Claude organises them and hands them back tidy. No coding.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Pro or Team, which includes **Cowork**).

1. Open **Claude.ai** and start a **Cowork** session (the workspace where you can drop files).
2. Drag in the sample files from this folder's **`sample_data/`** (`budget.xlsx`, `logo.png`,
   `notes.txt`, `script.py`, `video.mp4`) — or any messy files of your own.
3. Copy **the example prompt** below and paste it into the chat.
4. Claude sorts the files into category folders, shows you a summary table of what went
   where, and gives you the tidied result to download.

## The example prompt
Copy this exactly into Cowork after uploading your files:

```
I've uploaded a batch of random files. Please tidy them up for me.

1. Sort every file into a folder based on its type, using these categories:
   - Images (jpg, jpeg, png, gif, svg, webp)
   - Documents (pdf, doc, docx, txt, xls, xlsx, ppt, pptx, md)
   - Videos (mp4, mov, avi, mkv, webm)
   - Audio (mp3, wav, flac, m4a)
   - Code (py, js, html, css, json, yaml)
   - Archives (zip, tar, gz, rar, 7z)
   - Other (anything that doesn't fit above)

2. Show me a summary table: each category, how many files it got, and the filenames in it.
3. Put the sorted folders into a single zip I can download.
4. Don't rename or change the contents of any file — just move them into the right folder.
```

## Make it your own
- Swap the sample files for your real Downloads folder contents.
- Add your own categories — e.g. a "Receipts" folder for PDFs with "invoice" in the name.
- Ask Claude to also sort by **date** (e.g. one folder per month) instead of by type.

## Optional — automate it with code (advanced)
You do **not** need this for the course. If you later want to run the same sorting on your
own computer without uploading anything, **`main.py`** in this folder is a ready-to-run
Python script that does it. It uses only the Python standard library — no API key, nothing
to install. Run `python main.py sample_data/ --dry-run` to preview, then drop `--dry-run` to
apply. See the comments inside `main.py` for details.
