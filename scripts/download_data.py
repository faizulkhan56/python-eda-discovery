#!/usr/bin/env python3
"""Download the grades.csv dataset to ./data using only the standard library."""
import urllib.request
from pathlib import Path

DATA_URL = "https://raw.githubusercontent.com/Konami33/MlOps-Dataset/main/Data/grades.csv"
outdir = Path(__file__).resolve().parent.parent / "data"
outpath = outdir / "grades.csv"
outdir.mkdir(parents=True, exist_ok=True)

print(f"Downloading to: {outpath}")
urllib.request.urlretrieve(DATA_URL, outpath.as_posix())
print("Done.")
