#!/usr/bin/python3

import sys
import os
import re


def markdown2html(markdown_file, output_file):
    # Check if the markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Conversion logic from markdown to HTML goes here
    # You can use any Markdown to HTML converter library or tool

    # Placeholder implementation: copy the content of the markdown file to the output file
    with open(markdown_file, 'r') as md:
        markdown_content = md.read()

    # Perform any additional processing or conversion
    # Here, we replace '#' with '<h1>' tags
    html_content = re.sub(r'# (.+)', r'<h1>\1</h1>', markdown_content)

    with open(output_file, 'w') as html:
        html.write(html_content)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown2html(markdown_file, output_file)

    sys.exit(0)
