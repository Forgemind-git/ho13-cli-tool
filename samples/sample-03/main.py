"""
Batch Image Resizer — Starter Skeleton
TODO: Replace this skeleton with the script Claude generates for you in Cowork.

Steps:
1. Fill in cowork-prompt.md with your Cowork prompt
2. Upload a sample image to Claude Cowork (optional but helpful)
3. Claude will generate a complete Python script
4. Paste the generated script here, replacing this file
"""

import argparse
import sys
from pathlib import Path

# TODO: Add supported image extensions
SUPPORTED_EXTENSIONS = set()


def check_pillow():
    """TODO: Check that Pillow is installed; print a helpful message if not."""
    # TODO: Try to import PIL.Image, catch ImportError, print install instructions
    raise NotImplementedError("TODO: implement check_pillow()")


def resize_images(input_folder, output_folder, max_width, output_format=None):
    """TODO: Resize all images in input_folder and save to output_folder.

    Processing steps to implement:
    - List all supported image files in input_folder
    - For each image, resize to max_width keeping aspect ratio
    - Optionally convert to a different format
    - Save to output_folder
    - Track and report: count processed, total size before/after
    """
    raise NotImplementedError("TODO: implement resize_images()")


def main():
    parser = argparse.ArgumentParser(description="Batch Image Resizer")
    parser.add_argument("input_folder", help="Folder containing images to resize")
    parser.add_argument(
        "-o", "--output",
        help="Output folder (default: input_folder/resized/)"
    )
    parser.add_argument(
        "-w", "--width", type=int, default=800,
        help="Maximum width in pixels (default: 800)"
    )
    parser.add_argument(
        "-f", "--format",
        help="Output format, e.g. JPEG, PNG, WEBP (default: keep original)"
    )
    args = parser.parse_args()

    check_pillow()

    input_folder = Path(args.input_folder)
    if not input_folder.is_dir():
        print(f"[ERROR] Not a directory: {input_folder}")
        sys.exit(1)

    output_folder = Path(args.output) if args.output else input_folder / "resized"

    # TODO: Call resize_images
    resize_images(input_folder, output_folder, args.width, args.format)


if __name__ == "__main__":
    main()
