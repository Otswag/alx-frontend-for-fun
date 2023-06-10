#!/usr/bin/python3

import sys

import os

import markdown

import re

def markdown2html(markdown_file, output_file):

    # Check if the markdown file exists

    if not os.path.isfile(markdown_file):

        print(f"Missing {markdown_file}", file=sys.stderr)

        sys.exit(1)

    # Read the markdown file content

    with open(markdown_file, 'r') as md:

        markdown_content = md.read()

    # Convert markdown to HTML

    html_content = markdown.markdown(markdown_content)

    # Perform additional processing using regular expressions

    html_content = re.sub(r'<h1>', r'<h1 style="color: red;">', html_content)

    # Write the HTML content to the output file

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

