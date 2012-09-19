#!/usr/bin/env python2

import argparse
import sys

parser = argparse.ArgumentParser(description="Process some numbers.")
parser.add_argument("files", nargs="*", help="input files", type=file, default=[sys.stdin])
parser.add_argument("--ignore-blank", help="ignore blank lines", action="store_true")
parser.add_argument("--ignore-non-numeric", help="ignore non-numeric", action="store_true")
args = parser.parse_args()

product = 1
for f in args.files:
	for line in iter(f.readline, ''):
		line = line.strip()
		if line == "":
			if not args.ignore_blank:
				print product
				product = 1
			continue
		try:
			num = float(line)
			product *= num
		except ValueError as e:
			if not args.ignore_non_numeric:
				sys.stderr.write(str(e))
				sys.stderr.write("\n")
				sys.stderr.flush()
				sys.exit(1)

print product
