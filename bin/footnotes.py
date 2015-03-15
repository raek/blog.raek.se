#!/usr/bin/env python3

from sys import stdin, stdout
import re

next_number = 1

tag_numbers = {}

def superscript(number):
    result = ""
    for digit in str(number):
        if digit == '1':
            result += "&#x00B9;"
        elif digit in ['2', '3']:
            result += "&#x00B" + digit + ";"
        else:
            result += "&#x207" + digit + ";"
    return result;

def tag_number(tag):
    global next_number
    global tag_numbers
    if tag not in tag_numbers:
        tag_numbers[tag] = next_number
        next_number += 1
    return tag_numbers[tag]

def replace_reference_match(m):
    tag = m.group(1)
    number = tag_number(tag)
    return '<a name="footnote-reference%d" href="#footnote%d" class="footnote">%s</a>' % (number, number, superscript(number))

reference_pattern = re.compile(r'\(\(([^)]+)\)\)')

def replace_footnote_references(line):
    return reference_pattern.sub(replace_reference_match, line)

definition_pattern = re.compile(r'\(\(([^)]+)\)\):\s+(.*)', flags=re.DOTALL)

footnote_definitions = {}

def append_definition(tag, text):
    new_text = footnote_definitions.get(tag, "") + text
    footnote_definitions[tag] = new_text

current_definition = None
last_line_blank = True
line = stdin.readline()
while line:
    if not line.strip():
        stdout.write(line)
        current_definition = None
        last_line_blank = True
    else:
        m = definition_pattern.match(line)
        if m and last_line_blank:
            tag = m.group(1)
            text = replace_footnote_references(m.group(2))
            current_definition = tag
            append_definition(tag, text)
        elif current_definition is not None:
            text = replace_footnote_references(line)
            append_definition(current_definition, text)
        else:
            text = replace_footnote_references(line)
            stdout.write(text)
        last_line_blank = False
    line = stdin.readline()

if footnote_definitions:
    stdout.write("\n- - -\n")
    for tag, number in sorted(tag_numbers.items(), key=lambda x: x[1]):
        stdout.write("\n")
        stdout.write('%d. <a name="footnote%d"></a>' % (number, number))
        stdout.write(footnote_definitions[tag])
        stdout.write(' <a href="#footnote-reference%d" class="footnote-backlink">&#x21A9;</a>\n' % number)
