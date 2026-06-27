# Sample 01 — Smart Folder Sorter

Scans a folder, groups files by extension category (Images/Documents/Videos/Audio/Code/Archives/Other), and moves them into subfolders. `--dry-run` prints what it would do without moving.

## Install

```bash
pip install -r requirements.txt
```

No external dependencies — stdlib only.

## Usage

```bash
# Preview what would happen (safe, no files moved)
python main.py sample_data/ --dry-run

# Actually sort the folder
python main.py sample_data/

# Sort any folder on your system
python main.py /home/user/Downloads/
```

## Expected Output

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

## Categories

| Category  | Extensions                                              |
|-----------|---------------------------------------------------------|
| Images    | jpg, jpeg, png, gif, bmp, svg, webp, tiff, ico          |
| Documents | pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt, rtf, md |
| Videos    | mp4, avi, mov, mkv, wmv, flv, webm, m4v                |
| Audio     | mp3, wav, flac, aac, ogg, m4a                          |
| Code      | py, js, ts, html, css, java, cpp, c, go, rs, json, yaml |
| Archives  | zip, tar, gz, rar, 7z, bz2, xz, tgz                    |
| Other     | everything else                                         |

## Notes

- Only files directly in the source folder are moved (subdirectories are ignored).
- If a file with the same name already exists in the destination, it is renamed with a numeric suffix (e.g., `logo_1.png`).
