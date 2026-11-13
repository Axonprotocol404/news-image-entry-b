#!/usr/bin/env python3
# news-image-01: writes the 13 Nov 2026 world-news infographic to /output/entry.png
# The image is committed byte-for-byte as entry.png; this program only places it (no network).
# Placed at /output/entry.png by main.py.
import os, shutil
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), "/output/entry.png")
