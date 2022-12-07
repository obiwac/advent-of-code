import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

import numpy as np

f = open(0).read().strip().split('\n')

tree = {}

in_ls = False
curr = [] # abs path

for command in f:
	if in_ls and command[0] != '$':
		size, name = command.split()
		
		if size != 'dir':
			dir_ = tree

			for bit in curr:
				if bit in dir_:
					dir_ = dir_[bit]
				
				else:
					dir_[bit] = {}
					dir_ = dir_[bit]

			dir_[name] = int(size)

		continue

	in_ls = False

	if command[0] == '$':
		bits = command.split()

		if bits[1] == 'cd':
			path = bits[2].split('/')

			if not path[0] and not path[1]:
				curr = []

			elif not path[0]:
				curr = path[1:]

			elif path[0] == '..':
				curr.pop()

			else:
				curr += path

		elif bits[1] == 'ls':
			in_ls = True

total = 0
total_p1 = 0

def dfs1(tree):
	global total, total_p1
	dir_total = 0

	for k, v in tree.items():
		if type(v) == dict:
			size = dfs1(v)

			if size <= 1000000:
				total_p1 += size

			total += size
			dir_total += size

		else:
			dir_total += v

	return dir_total

size = dfs1(tree)

if size <= 1000000:
	total_p1 += size

total += size
free = 70000000 - total
needed = 30000000
need_to_free = needed - free

candidates = []

def dfs(tree):
	dir_total = 0

	for k, v in tree.items():
		if type(v) == dict:
			size = dfs(v)

			if size >= need_to_free:
				candidates.append(size)

			dir_total += size

		else:
			dir_total += v

	return dir_total

size = dfs(tree)

if size >= need_to_free:
	candidates.append(size)

print("p1:", total_p1)
print("p2:", min(candidates))
