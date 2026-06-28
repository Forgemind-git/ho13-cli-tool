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

---

## Optional — automate it with code (advanced)
You do **not** need this for the course. The included **`main.py`** is the worked reference
script: a command-line **Smart Folder Sorter** that does the same job on your own computer.
It groups files by extension category and moves them into subfolders. `--dry-run` prints
what it would do without moving anything. It uses only the Python standard library — no API
key, nothing to install.

### Run it

```bash
# Preview what would happen (safe, no files moved)
python main.py sample_data/ --dry-run

# Actually sort the folder
python main.py sample_data/

# Sort any folder on your system
python main.py /home/user/Downloads/
```

### Expected output

```
[DRY RUN] Sorting 5 file(s) in: /path/to/sample_data

  [WOULD MOVE] budget.xlsx -> Documents/
  [WOULD MOVE] logo.png -> Images/
  [WOULD MOVE] notes.txt -> Documents/
  [WOULD MOVE] script.py -> Code/
  [WOULD MOVE] video.mp4 -> Videos/

=============================================
  SUMMARY — Would move 5 file(s)
=============================================
  Code          (1 file(s))
    - script.py
  Documents     (2 file(s))
    - budget.xlsx
    - notes.txt
  Images        (1 file(s))
    - logo.png
  Videos        (1 file(s))
    - video.mp4
=============================================

  [DRY RUN] No files were actually moved.
  Run without --dry-run to apply changes.
```

### Categories

| Category  | Extensions                                              |
|-----------|---------------------------------------------------------|
| Images    | jpg, jpeg, png, gif, bmp, svg, webp, tiff, ico          |
| Documents | pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt, rtf, md |
| Videos    | mp4, avi, mov, mkv, wmv, flv, webm, m4v                |
| Audio     | mp3, wav, flac, aac, ogg, m4a                          |
| Code      | py, js, ts, html, css, java, cpp, c, go, rs, json, yaml |
| Archives  | zip, tar, gz, rar, 7z, bz2, xz, tgz                    |
| Other     | everything else                                         |

### Notes
- Only files directly in the source folder are moved (subdirectories are ignored).
- If a file with the same name already exists in the destination, it is renamed with a
  numeric suffix (e.g., `logo_1.png`).
