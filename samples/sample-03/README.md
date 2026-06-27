# Sample 03 — Batch Image Resizer

Resizes all images in a folder to the given max width (keeping aspect ratio), optionally converts format, and saves to an output folder. Reports count and total size saved.

## Install

```bash
pip install -r requirements.txt
```

Requires **Pillow** for image processing.

## Usage

```bash
# Resize all images to max 800px wide, save to output/
python main.py sample_data/ --width 800

# Resize and convert to WebP format
python main.py sample_data/ --width 1920 --format webp

# Specify custom output folder
python main.py photos/ --width 640 --output thumbs/ --format jpg
```

## Expected Output

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

## Supported Formats

Input and output: `jpg`, `jpeg`, `png`, `bmp`, `gif`, `tiff`, `webp`

## Notes

- If an image is already smaller than `--width`, it is copied as-is (no upscaling).
- JPEG output uses quality 88 with optimisation enabled.
- RGBA/transparent PNGs converted to JPEG get a white background.
- The `sample_data/` folder contains placeholder files. Replace them with real images.

## Sample Data

The `sample_data/` folder contains placeholder `.txt` files with instructions on how to add real images for testing. Replace these with actual image files to test the resizer.
