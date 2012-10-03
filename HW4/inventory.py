from __future__ import print_function
import argparse
import ast
import csv
import sys

data = []

def insert_record(data, args):
	data.append(ast.literal_eval(args))
	print('Inserted 1 record(s).')

def delete_record(data, args):
	key, value = args.split('=', 1)
	if key not in fields:
		print("ERROR: '{}' is not a valid field".format(key), file=sys.stderr)
		return

	to_remove = []
	for row in data:
		if row[key] == value:
			to_remove.append(row)
	for row in to_remove:
		data.remove(row)
	print('Deleted {} record(s)'.format(len(to_remove)))

def update_record(data, args):
	update, condition = args.split(' where ', 1)
	up_key, up_val = update.split('=', 1)
	cond_key, cond_val = condition.split('=', 1)
	if up_key not in fields:
		print("ERROR: '{}' is not a valid field".format(up_key), file=sys.stderr)
		return
	if cond_key not in fields:
		print("ERROR: '{}' is not a valid field".format(cond_key), file=sys.stderr)
		return
	
	if up_key == 'Quantity':
		up_val = int(up_val)

	if cond_key == 'Quantity':
		cond_val = int(cond_val)

	updated = 0
	for row in data:
		if row[cond_key] == cond_val:
			row[up_key] = up_val
			updated += 1
	
	print('Updated {} record(s)'.format(updated))

def select_record(data, args):
	if ' sort by ' in args:
		args, sort_field = args.split(' sort by ', 1)
		data = sorted(data, key=lambda x: x[sort_field])

	cond = lambda x: True
	if ' where ' in args:
		args, condition = args.split(' where ', 1)
		cond_key, cond_val = condition.split('=', 1)
		if cond_key == 'Quantity':
			cond_val = int(cond_val)
		cond = lambda x: x[cond_key] == cond_val

	data = filter(cond, data)

	for row in data:
		print(row)
	
	print('Displayed {} record(s)'.format(len(data)))

commands = {
	'insert': insert_record,
	'delete': delete_record,
	'update': update_record,
	'select': select_record,
}

fields = []

def main():
	global data, fields

	parser = argparse.ArgumentParser("Work with a simple inventory database")
	parser.add_argument("-f", "--data-file", required=True, help="path to the data file to read at startup")
	args = parser.parse_args()

	with open(args.data_file) as f:
		reader = csv.DictReader(f, doublequote=False, escapechar='\\', quoting=csv.QUOTE_NONNUMERIC)
		fields = reader.fieldnames
		data = [val for val in reader]

	for row in data:
		row['Quantity'] = int(row['Quantity'])

	for line in iter(sys.stdin.readline, ""):
		cmd = line.rstrip('\n').split(None, 1)
		if len(cmd) > 1:
			rest = cmd[1]
		else:
			rest = ''
		cmd = cmd[0]
		if cmd in commands:
			commands[cmd](data, rest)
		else:
			print("No such command '{}'.".format(cmd), file=sys.stderr)

if __name__ == "__main__":
	main()