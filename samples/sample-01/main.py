"""
Smart Folder Sorter
Scans a folder, groups files by extension category, and moves them into subfolders.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

# Category definitions: extension -> folder name
CATEGORIES = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".bmp": "Images", ".svg": "Images", ".webp": "Images", ".tiff": "Images", ".ico": "Images",
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents", ".pptx": "Documents",
    ".odt": "Documents", ".rtf": "Documents", ".md": "Documents",
    ".mp4": "Videos", ".avi": "Videos", ".mov": "Videos", ".mkv": "Videos",
    ".wmv": "Videos", ".flv": "Videos", ".webm": "Videos", ".m4v": "Videos",
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".aac": "Audio",
    ".ogg": "Audio", ".m4a": "Audio",
    ".py": "Code", ".js": "Code", ".ts": "Code", ".html": "Code", ".css": "Code",
    ".java": "Code", ".cpp": "Code", ".c": "Code", ".h": "Code", ".go": "Code",
    ".rs": "Code", ".rb": "Code", ".php": "Code", ".sh": "Code", ".json": "Code",
    ".xml": "Code", ".yaml": "Code", ".yml": "Code", ".toml": "Code", ".ini": "Code",
    ".zip": "Archives", ".tar": "Archives", ".gz": "Archives", ".rar": "Archives",
    ".7z": "Archives", ".bz2": "Archives", ".xz": "Archives", ".tgz": "Archives",
}


def get_category(filepath):
    ext = filepath.suffix.lower()
    return CATEGORIES.get(ext, "Other")


def sort_folder(source, dry_run=False):
    if not source.exists():
        print(f"[ERROR] Folder does not exist: {source}")
        sys.exit(1)
    if not source.is_dir():
        print(f"[ERROR] Path is not a folder: {source}")
        sys.exit(1)

    files = [f for f in source.iterdir() if f.is_file()]

    if not files:
        print(f"[INFO] No files found in: {source}")
        return {}

    summary = {}
    moved_count = 0

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Sorting {len(files)} file(s) in: {source}\n")

    for filepath in sorted(files):
        category = get_category(filepath)
        dest_dir = source / category
        dest_path = dest_dir / filepath.name
        summary.setdefault(category, []).append(filepath.name)

        if dry_run:
            print(f"  [WOULD MOVE] {filepath.name} -> {category}/")
        else:
            dest_dir.mkdir(exist_ok=True)
            if dest_path.exists():
                stem = filepath.stem
                suffix = filepath.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
                print(f"  [RENAMED]  {filepath.name} -> {category}/{dest_path.name}")
            else:
                print(f"  [MOVED]    {filepath.name} -> {category}/")
            try:
                shutil.move(str(filepath), str(dest_path))
                moved_count += 1
            except Exception as e:
                print(f"  [ERROR]    Failed to move {filepath.name}: {e}")

    return summary


def print_summary(summary, dry_run):
    if not summary:
        return
    total = sum(len(v) for v in summary.values())
    action = "Would move" if dry_run else "Moved"
    print(f"\n{'='*45}")
    print(f"  SUMMARY — {action} {total} file(s)")
    print(f"{'='*45}")
    for category, files in sorted(summary.items()):
        print(f"  {category:12s}  ({len(files)} file(s))")
        for fname in files:
            print(f"    - {fname}")
    print(f"{'='*45}\n")
    if dry_run:
        print("  [DRY RUN] No files were actually moved.")
        print("  Run without --dry-run to apply changes.\n")


def main():
    parser = argparse.ArgumentParser(
        prog="folder-sorter",
        description=(
            "Smart Folder Sorter — Scans a folder and moves files into category "
            "subfolders: Images, Documents, Videos, Audio, Code, Archives, Other."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py sample_data/
  python main.py sample_data/ --dry-run
  python main.py /home/user/Downloads/
        """,
    )
    parser.add_argument("source_folder", help="Path to the folder you want to sort")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview what would happen without moving any files"
    )
    args = parser.parse_args()
    source = Path(args.source_folder).resolve()
    summary = sort_folder(source, dry_run=args.dry_run)
    print_summary(summary, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
