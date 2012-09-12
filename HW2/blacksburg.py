# ECE 2524 Homework 2 Problem 2 Joseph Callen

import sys
if len(sys.argv) < 2:
	print >>sys.stderr, "Usage: %s filename" % sys.argv[0]
	sys.exit(1)
	
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open(sys.argv[1]) as f:
	for line in f:
		fields = line.split()
		if fields[3] == "Blacksburg":
			print ", ".join((fields[4], fields[1], fields[0], fields[2]))
