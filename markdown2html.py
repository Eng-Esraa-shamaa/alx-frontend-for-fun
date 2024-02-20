#!/usr/bin/python3
"""
Markdown to HTML
"""
import sys
import os.path
import re


def convert_heading(line):
    """
    convert to heading levels
    """
    match = re.match(r'^(#+)\s+(.+)', line)
    if match:
        h_level = len(match.group(1))
        h_text = match.group(2)
        return f'<h{h_level}>{h_text}</h{h_level}>'
    else:
        return line


def markdown_to_html(markdown_lines):
    """
    to convert to html
    """
    html_lines = [convert_heading(line) for line in markdown_lines]
    return '\n'.join(html_lines)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as f:
        markdown_content = f.read().splitlines()

    html_content = markdown_to_html(markdown_content)

    with open(sys.argv[2], 'w') as f:
        f.write(html_content)

    sys.exit(0)
