#!/usr/bin/env python3

from pathlib import Path

posts_dir = Path("src", "posts")
for json_path in posts_dir.glob("**/post.json"):
    print(json_path.parent.relative_to(posts_dir))
