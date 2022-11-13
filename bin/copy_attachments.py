#!/usr/bin/env python3

import os
from pathlib import Path
from shutil import copytree, rmtree


posts_dir = Path("src", "posts")
site_out_dir = Path("out", os.environ["SITE"])

for src_files_dir in posts_dir.glob("**/files") :
    if not src_files_dir.is_dir():
        continue
    dst_files_dir = site_out_dir / src_files_dir.relative_to(posts_dir)
    if dst_files_dir.exists():
        rmtree(dst_files_dir)
    copytree(src_files_dir, dst_files_dir)
