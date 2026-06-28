# Cowork Prompt: image resizer

## What to paste into Cowork

Upload a few images first (any JPG or PNG — you can use `logo.png` from Sample 1's
`sample_data/` to try it out), then paste this:

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

---

**Example structure to adapt:**

> I need a Python script that resizes all images in a folder.
> Requirements:
> - Max width: [TODO: your target width, e.g. 1200px]
> - Keep aspect ratio (don't stretch or crop)
> - Output format: [TODO: e.g. JPEG, PNG, or keep original]
> - Save resized files to a subfolder called "resized/"
> - Print a summary: how many images processed and total size saved
> Use the Pillow library. No other dependencies.
