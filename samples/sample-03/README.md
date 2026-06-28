# HO13 Sample 3 — Resize a Batch of Images

## What you'll build
A batch image helper. Instead of opening photos one by one to shrink them, you drop a whole
set into Claude and ask it to resize them all at once — perfect for web uploads, email
attachments, or trimming a folder that's eating your disk space. No coding.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Pro or Team, which includes **Cowork**).

1. Open **Claude.ai** and start a **Cowork** session (the workspace where you can drop files).
2. Drag in a few images of your own (JPG or PNG). You can also use the `logo.png` from
   Sample 1's `sample_data/` to try it out.
3. Copy **the example prompt** below and paste it into the chat.
4. Claude resizes every image, tells you the before/after sizes, and gives you the smaller
   versions to download.

## The example prompt
Copy this exactly into Cowork after uploading your images:

```
I've uploaded several images. Please resize all of them in one go.

Rules:
1. Make each image at most 800 pixels wide, keeping the original aspect ratio (no stretching).
2. If an image is already 800px wide or smaller, leave its size as-is — don't enlarge it.
3. Convert them all to WebP to save space (keep the same base filenames).
4. Show me a table: for each image, the original size in pixels and MB, and the new size,
   and how much space was saved overall.
5. Put the resized images into a single zip I can download.
```

## Make it your own
- Change `800` to whatever width you need (e.g. 1920 for full-screen, 400 for thumbnails).
- Ask for JPG instead of WebP if you need maximum compatibility.
- Ask Claude to also add your logo as a small watermark in the corner.

## Optional — automate it with code (advanced)
You do **not** need this for the course. If you later want to resize folders on your own
computer, **`main.py`** in this folder is a ready-to-run Python script that does it. It uses
the **Pillow** library — install it once with `pip install -r requirements.txt`, then run
`python main.py sample_data/ --width 800 --format webp`. See the comments inside `main.py`.
