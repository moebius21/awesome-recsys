#!/usr/bin/env python3
"""Download an official MovieLens archive for classroom use."""
import argparse
import hashlib
import shutil
import urllib.request
import zipfile
from pathlib import Path

URLS = {
    "100k": "https://files.grouplens.org/datasets/movielens/ml-100k.zip",
    "1m": "https://files.grouplens.org/datasets/movielens/ml-1m.zip",
    "20m": "https://files.grouplens.org/datasets/movielens/ml-20m.zip",
    "32m": "https://files.grouplens.org/datasets/movielens/ml-32m.zip",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", choices=URLS, default="100k")
    parser.add_argument("--output", type=Path, default=Path("data/raw"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    archive = args.output / f"ml-{args.size}.zip"
    print(f"Downloading {URLS[args.size]} ...")
    with urllib.request.urlopen(URLS[args.size]) as src, archive.open("wb") as dst:
        shutil.copyfileobj(src, dst)
    print(f"Downloaded {archive} ({archive.stat().st_size:,} bytes)")
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(args.output)
    print("Extracted. Please record the download date and verify the official README.")

if __name__ == "__main__":
    main()
