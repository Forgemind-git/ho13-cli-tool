# Cowork Prompt: folder sorter

## What to paste into Cowork

Upload the sample files first (`sample_data/budget.xlsx`, `logo.png`, `notes.txt`,
`script.py`, `video.mp4` — or your own messy files), then paste this:

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

---

**Example structure to adapt:**

> I have uploaded a text file containing a list of filenames from my Downloads folder.
> Please sort these filenames into categories (Images, Documents, Videos, Code, Archives, Other)
> and generate a Python script that will move each file into the correct subfolder.
> Also show a summary table of how many files go into each category.
