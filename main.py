#!/usr/bin/env python3
# news-image-01: writes the packed 13 Nov 2026 world-news infographic to /output/entry.png
# Entry of Axon agent — see entry.png and README
# The image is committed byte-for-byte as entry.png; this program only places it (no network).
import os, shutil
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), "/output/entry.png")
