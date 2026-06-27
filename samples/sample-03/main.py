"""
Batch Image Resizer
Resizes all images in a folder to the given max width (keeping aspect ratio),
optionally converts format, and saves to an output folder.
"""

import argparse
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}


def check_pillow():
    try:
        from PIL import Image
        return Image
    except ImportError:
        print("[ERROR] Pillow is not installed.")
        print("  Install it with:  pip install Pillow")
        sys.exit(1)


def resize_images(source_dir, max_width, output_dir, output_format=None):
    Image = check_pillow()

    source = Path(source_dir)
    if not source.exists() or not source.is_dir():
        print(f"[ERROR] Source folder not found: {source}")
        sys.exit(1)

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    # Collect image files
    image_files = [
        f for f in sorted(source.iterdir())
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not image_files:
        print(f"[INFO] No supported image files found in: {source}")
        print(f"  Supported formats: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        return

    fmt = output_format.upper() if output_format else None
    # Map common aliases
    fmt_map = {"JPG": "JPEG"}
    if fmt in fmt_map:
        fmt = fmt_map[fmt]

    ext_map = {"JPEG": ".jpg", "PNG": ".png", "WEBP": ".webp", "BMP": ".bmp", "TIFF": ".tiff"}

    total_original_bytes = 0
    total_output_bytes = 0
    processed = 0
    skipped = 0

    print(f"\nResizing {len(image_files)} image(s) from: {source}")
    print(f"  Max width   : {max_width}px")
    print(f"  Output dir  : {output}")
    print(f"  Format      : {fmt if fmt else 'keep original'}\n")

    for img_path in image_files:
        try:
            original_size = img_path.stat().st_size
            total_original_bytes += original_size

            with Image.open(img_path) as img:
                orig_w, orig_h = img.size

                # Determine output extension and format
                save_fmt = fmt if fmt else img.format or "JPEG"
                if save_fmt in fmt_map.values() or save_fmt == "JPEG":
                    out_ext = ".jpg"
                elif save_fmt in ext_map:
                    out_ext = ext_map[save_fmt]
                else:
                    out_ext = img_path.suffix.lower()

                out_filename = img_path.stem + out_ext
                out_path = output / out_filename

                # Check if resize is needed
                if orig_w <= max_width:
                    new_w, new_h = orig_w, orig_h
                    resized = False
                else:
                    ratio = max_width / orig_w
                    new_w = max_width
                    new_h = int(orig_h * ratio)
                    resized = True

                # Convert RGBA -> RGB for JPEG
                save_img = img
                if save_fmt == "JPEG" and img.mode in ("RGBA", "P", "LA"):
                    bg = Image.new("RGB", img.size, (255, 255, 255))
                    if img.mode == "P":
                        img = img.convert("RGBA")
                    bg.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
                    save_img = bg

                if resized:
                    save_img = save_img.resize((new_w, new_h), Image.LANCZOS)

                save_img.save(out_path, format=save_fmt, quality=88, optimize=True)
                output_size = out_path.stat().st_size
                total_output_bytes += output_size

                saved_pct = (1 - output_size / original_size) * 100 if original_size else 0
                resize_tag = f"{orig_w}x{orig_h} -> {new_w}x{new_h}" if resized else f"{orig_w}x{orig_h} (no resize)"
                print(
                    f"  [OK] {img_path.name:30s}  {resize_tag}  "
                    f"{_fmt_bytes(original_size)} -> {_fmt_bytes(output_size)} "
                    f"({saved_pct:+.0f}%)"
                )
                processed += 1

        except Exception as e:
            print(f"  [SKIP] {img_path.name}: {e}")
            skipped += 1

    saved_bytes = total_original_bytes - total_output_bytes
    print(f"\n{'='*55}")
    print(f"  SUMMARY")
    print(f"{'='*55}")
    print(f"  Processed   : {processed} image(s)")
    if skipped:
        print(f"  Skipped     : {skipped} file(s) (errors)")
    print(f"  Original    : {_fmt_bytes(total_original_bytes)}")
    print(f"  Output      : {_fmt_bytes(total_output_bytes)}")
    print(f"  Space saved : {_fmt_bytes(abs(saved_bytes))} "
          f"({'saved' if saved_bytes >= 0 else 'larger'})")
    print(f"  Output dir  : {output}")
    print(f"{'='*55}\n")


def _fmt_bytes(n):
    if n < 1024:
        return f"{n} B"
    elif n < 1024 ** 2:
        return f"{n/1024:.1f} KB"
    else:
        return f"{n/1024**2:.2f} MB"


def main():
    parser = argparse.ArgumentParser(
        prog="image-resizer",
        description=(
            "Batch Image Resizer — Resizes all images in a folder to the given max width "
            "(keeping aspect ratio), optionally converts format, and saves to an output folder."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py sample_data/ --width 800
  python main.py sample_data/ --width 1920 --format webp
  python main.py photos/ --width 640 --output thumbs/ --format jpg
        """,
    )
    parser.add_argument("folder", help="Folder containing images to resize")
    parser.add_argument("--width", "-w", type=int, required=True,
                        help="Maximum width in pixels (height is scaled proportionally)")
    parser.add_argument("--format", "-f", default=None,
                        help="Output format: jpg, png, webp, bmp, tiff (default: keep original)")
    parser.add_argument("--output", "-o", default="output",
                        help="Output folder (default: output/)")

    args = parser.parse_args()

    if args.width <= 0:
        print("[ERROR] --width must be a positive integer.")
        sys.exit(1)

    resize_images(
        source_dir=args.folder,
        max_width=args.width,
        output_dir=args.output,
        output_format=args.format,
    )


if __name__ == "__main__":
    main()
