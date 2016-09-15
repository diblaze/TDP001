#! /usr/bin/env python3
# Created by Denis Ivan Blazevic - denbl369@liu.se
# Date: 2016-08-20
# Summary: This script searches for all HTML tag occureces in a specific file and then prints out the tag and how many times it occurs.

import re
import argparse
import sys

# Adding CLI-arguments so user can pass files into the script
parser = argparse.ArgumentParser()
parser.add_argument("f", help="File to read")
args = parser.parse_args()

# Open the passed file and read all
with open(args.f, 'r') as f:
    contents = f.read();

# Find all HTML tag occurences with RegEX
html_tag_matches = re.findall("(<[^/!].\S*>|<[^/!].\S*)", contents)

# If there are no HTML tags, quit the script with an error message.
if not html_tag_matches:
    print("Script created by denbl369@liu.se, 2016-08-20")
    print("No HTML tags in the " + args.f + " file.")
    sys.exit()

# Show who created the script.
print("Script created by denbl369@liu.se, 2016-08-20")

# Go through each found HTML tag and check if they end with a '>'
# If not - add '>' to the end of the tag.
for i, tag in enumerate(html_tag_matches):
    if not tag.endswith(">"):
        html_tag_matches[i] = tag + ">"

# Count how many times a HTML tag occurs in the list and then prints out in style of "[COUNT] [HTML TAG]"
# If the tag occurs more than once, remove all other occurences before printing.
for tag in html_tag_matches:
    tag_count = html_tag_matches.count(tag)
    print(str(tag_count) + " " + tag)
    if tag_count > 1:
        for i in range(0, tag_count):
            html_tag_matches.remove(tag)
            
    


