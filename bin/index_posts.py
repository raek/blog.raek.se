#!/usr/bin/env python3

import itertools
import json
from operator import itemgetter
from pathlib import Path
import sys

posts = []

for line in sys.stdin:
    post_json_path = Path("src", "posts", line.rstrip(), "post.json")
    with post_json_path.open("r", encoding="utf-8") as f:
        post = json.load(f)
    if not post.get("draft", False):
        posts.append(post)

posts.sort(key=itemgetter("datePublished"), reverse=True)

def post_year(post):
    date = post["datePublished"]
    year = date.split("-")[0]
    return year

years = []
for year, posts in itertools.groupby(posts, post_year):
    years.append({"year": year, "posts": list(posts)})

output = {"years": years}
json.dump(output, sys.stdout, indent=4, sort_keys=True)
