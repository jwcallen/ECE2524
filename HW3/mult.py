#!/usr/bin/env python2

import argparse
import sys

parser = argparse.ArgumentParser(description="Process some numbers.")
parser.parse_args()

product = 1
for line in iter(sys.stdin.readline, ""):
	line = line.rstrip("\n")
	if line == "":
		print product
		product = 1
		continue
	try:
		num = float(line)
		product *= num
	except ValueError as e:
		sys.stderr.write(str(e))
		sys.stderr.write("\n")
		sys.stderr.flush()
		sys.exit(1)

print product
