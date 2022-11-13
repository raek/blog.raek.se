#!/usr/bin/env python3

from argparse import ArgumentParser
import json


parser = ArgumentParser()
parser.add_argument("json_file")
parser.add_argument("path")
args = parser.parse_args()

assert args.path.startswith(".")
key = args.path[1:]
assert "." not in key and "[" not in key

with open(args.json_file, "r", encoding="utf-8") as f:
    j = json.load(f)
print(j[key])
