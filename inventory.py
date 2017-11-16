#inventory script for TextGame

import sys

inventory = set()

def get():
	j = 0
	print("\nYour inventory contains:")
	for i in inventory:
		j += 1
		sys.stdout.write(i)
		if j < len(inventory):
			sys.stdout.write(", ")
		elif j == len(inventory):
			print("")

def add(item):
	item = item.lower()
	if item not in inventory:
		inventory.add(item)
		return 0
	else:
		return 1

def remove(item):
	item = item.lower()
	if item in inventory:
		inventory.remove(item)
		return 0
	else:
		return 1
