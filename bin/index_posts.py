#!/usr/bin/env python3

import os
import itertools
import json
import sys

posts = []

for line in sys.stdin:
    post_json_file = os.path.join(
        os.environ["BLOG_DIR"],
        "src", "posts",
        line.rstrip(),
        "post.json")
    post = json.load(open(post_json_file, "r"))
    posts.append(post)

posts.sort(
    key=lambda post:
            post["datePublished"],
    reverse=True)

years = []
for year, posts in itertools.groupby(posts, lambda post: post["datePublished"].split("-")[0]):
    years.append({"year": year, "posts": list(posts)})

output = {"years": years}
json.dump(output, sys.stdout, indent=4, sort_keys=True)
