"""
Smart Folder Sorter — Starter Skeleton
TODO: Replace this skeleton with the script Claude generates for you in Cowork.

Steps:
1. Fill in cowork-prompt.md with your Cowork prompt
2. Upload your file list to Claude Cowork
3. Claude will generate a complete Python script
4. Paste the generated script here, replacing this file
"""

import argparse
from pathlib import Path


# TODO: Define your file categories here
# Example:
# CATEGORIES = {
#     ".jpg": "Images",
#     ".pdf": "Documents",
#     ...
# }
CATEGORIES = {}


def get_category(filepath):
    """TODO: Return the category name for a given file path."""
    # TODO: Look up the file extension in CATEGORIES
    # Return "Other" if not found
    raise NotImplementedError("TODO: implement get_category()")


def sort_folder(source, dry_run=False):
    """TODO: Scan source folder and sort files into category subfolders."""
    # TODO:
    # 1. Check source exists and is a directory
    # 2. List all files (not subdirectories)
    # 3. For each file, determine its category
    # 4. If dry_run: print what would happen
    # 5. If not dry_run: create the subfolder and move the file
    # 6. Return a summary dict: {category: [list of filenames]}
    raise NotImplementedError("TODO: implement sort_folder()")


def print_summary(summary, dry_run):
    """TODO: Print a formatted summary of what was (or would be) moved."""
    # TODO: Print totals and per-category breakdown
    raise NotImplementedError("TODO: implement print_summary()")


def main():
    parser = argparse.ArgumentParser(description="Smart Folder Sorter")
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
