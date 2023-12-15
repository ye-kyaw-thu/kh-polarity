"""
Last updated: 14 Dec 2023
@author: Ye Kyaw Thu, Affiliate Professor, CADT, Phnom Penh, Cambodia

How to Run:
$ python ./zwsp_or_u200b_cleaner.py --help
$ python ./zwsp_or_u200b_cleaner.py --input kh-polar.shuf.clean.txt \
--output kh-polar.ver1.0.txt
"""

import sys
import argparse
import re

def clean_text(text):
    # Remove Zero Width Spaces
    return re.sub(u'\u200B', '', text)

def process_input(input_stream):
    return [clean_text(line) for line in input_stream]

def main():
    parser = argparse.ArgumentParser(description="Clean text by removing Zero Width Spaces (ZWSP) or U200B.")
    parser.add_argument('-i', '--input', nargs='?', type=str, default=sys.stdin,
                        help="Input file path. Reads from stdin if no file is provided.")
    parser.add_argument('-o', '--output', nargs='?', type=str, default=sys.stdout,
                        help="Output file path. Writes to stdout if no file is provided.")

    args = parser.parse_args()

    # Handling input
    if args.input is sys.stdin:
        input_stream = sys.stdin
    else:
        input_stream = open(args.input, 'r', encoding='utf-8')

    cleaned_lines = process_input(input_stream)

    # Handling output
    if args.output is sys.stdout:
        output_stream = sys.stdout
    else:
        output_stream = open(args.output, 'w', encoding='utf-8')

    for line in cleaned_lines:
        print(line, end='', file=output_stream)

    # Close the files if they are not stdin or stdout
    if input_stream is not sys.stdin:
        input_stream.close()
    if output_stream is not sys.stdout:
        output_stream.close()

if __name__ == "__main__":
    main()
