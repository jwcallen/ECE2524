# ECE 2524 Homework 2 Problem 1 Joseph Callen

import sys
if len(sys.argv) < 2:
	print "Usage: %s filename" % sys.argv[0]
	sys.exit(1)
else:
	name = sys.argv[1]

with open(name, "r") as f:
	for line in f:
		fields = line.rstrip().split(':')
		print "%s\t%s" % (fields[0], fields[6])


