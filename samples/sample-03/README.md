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

---

## Optional — automate it with code (advanced)
You do **not** need this for the course. The included **`main.py`** is the worked reference
script: a command-line **Batch Image Resizer** that does the same job on your own computer.
It resizes every image in a folder to a max width (keeping aspect ratio), optionally converts
format, and reports total size saved. It uses the **Pillow** library.

### Install and run

```bash
pip install -r requirements.txt

# Resize all images to max 800px wide, save to output/
python main.py sample_data/ --width 800

# Resize and convert to WebP format
python main.py sample_data/ --width 1920 --format webp

# Specify custom output folder
python main.py photos/ --width 640 --output thumbs/ --format jpg
```

### Expected output

```
Resizing 3 image(s) from: sample_data
  Max width   : 800px
  Output dir  : output
  Format      : keep original

  [OK] photo_large.jpg          2400x1600 -> 800x533   3.20 MB -> 0.45 MB (-86%)
  [OK] banner.png               1200x400  -> 800x267   1.10 MB -> 0.38 MB (-65%)
  [OK] icon.png                 64x64     64x64 (no resize)   4.2 KB -> 4.1 KB (-2%)

=======================================================
  SUMMARY
=======================================================
  Processed   : 3 image(s)
  Original    : 4.33 MB
  Output      : 0.83 MB
  Space saved : 3.50 MB (saved)
  Output dir  : output
=======================================================
```

### Supported formats
Input and output: `jpg`, `jpeg`, `png`, `bmp`, `gif`, `tiff`, `webp`

### Notes
- If an image is already smaller than `--width`, it is copied as-is (no upscaling).
- JPEG output uses quality 88 with optimisation enabled.
- RGBA/transparent PNGs converted to JPEG get a white background.
- The `sample_data/` folder contains a placeholder `.txt` with instructions for adding real
  images. Replace it with actual image files to test the resizer.
