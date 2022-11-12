#!/usr/bin/env python3

from collections import namedtuple
import json
from io import TextIOWrapper
import sys


Section = namedtuple("Section", "name, type, file")


def main():
    sections = parse_args()
    output = read_sections(sections)
    print(json.dumps(output))


def parse_args():
    for arg in sys.argv[1:]:
        parts = arg.split(":", maxsplit=2)
        assert len(parts) == 3
        assert parts[1] in ["str", "json"]
        yield Section(*parts)


def read_sections(sections):
    result = {}
    for section in sections:
        with open(section.file, "r", encoding="utf-8") as f:
            if section.type == "str":
                value = f.read()
            elif section.type == "json":
                value = json.load(f)
            else:
                raise ValueError(section.type)
        result[section.name] = value
    return result


if __name__ == "__main__":
    main()
