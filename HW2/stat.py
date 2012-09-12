# ECE 2524 Homework 2 Problem 3 Joseph Callen

import sys
if len(sys.argv) < 2:
	print >>sys.stderr, "Usage: %s filename" % sys.argv[0]
	sys.exit(1)

total = 0.0
max = float('-inf')
min = float('inf')
max_name = None
min_name = None
count = 0

with open(sys.argv[1]) as f:
	for line in f:
		fields = line.split()
		value = float(fields[2])
		total += value
		count += 1
		if value > max:
			max = value
			max_name = fields[1]
		if value < min:
			min = value
			min_name = fields[1]


print "ACCOUNT SUMMARY"
print "Total amount owed = %.2f" %total
print "Average amount owed = %.2f" % (total / count)
print "Maximimum amount owed = %.2f by %s" % (max, max_name)
print "Minimum amount owed = %.2f by %s" % (min, min_name)
