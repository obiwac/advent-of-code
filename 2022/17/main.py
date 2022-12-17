import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import heapq

*f, = open(0).read().strip()

# TETRIS!

shapes = [
"####",

""".#.
###
.#.""",

"""..#
..#
###""",

"""#
#
#
#""",

"""##
##"""
		]

m = [["."] * 7 for _ in range(500000)]
waterline = 0
SURENESS = 5

def pm(m, h = waterline):
	print("===")
	for l in map("".join, reversed(m[h - 10: h])):
		print(l)

def hm(m, h = waterline):
	return hash(tuple(map("".join, reversed(m[h - SURENESS: h])))) # prolly don't need to go as high

a = 0
fi = 0
waterlines = [0] # should be 2 * lcm large (adding 0 so we can index from 1)
targ = 1000000000000
seen = {} # key: hash, value: waterline

while 1:
	si = a % len(shapes)
	shape = shapes[si].split('\n')
	x, y = 2, waterline + 3

	# simulate falling

	while 1:
		# fall

		y -= 1

		# push

		o = x
		c = f[fi]
		fi = (fi + 1) % len(f)
		x += 1 if c == '>' else -1
		x = max(x, 0)
		x = min(x, 7 - len(shape[0]))

		# check we don't collide with anything (horizontal)

		hstop = False

		for j in range(len(shape)):
			for i in range(len(shape[0])):
				if m[y + j + 1][x + i] == '#' and shape[len(shape) - j - 1][i] == '#':
					hstop = True

		if hstop:
			x = o

		# check we don't collide with anything (vertical)

		vstop = y < 0

		for j in range(len(shape)):
			for i in range(len(shape[0])):
				if m[y + j][x + i] == '#' and shape[len(shape) - j - 1][i] == '#':
					vstop = True

		if vstop:
			y += 1

		if vstop:
			for j in range(len(shape)):
				for i in range(len(shape[0])):
					if shape[len(shape) - j - 1][i] == '#':
						m[y + j][x + i] = '#'
						waterline = max(y + j + 1, waterline)

			break

	a += 1
	waterlines.append(waterline)

	if a <= SURENESS:
		continue

	h = hm(m, waterline) ^ hash(fi) ^ hash(si)

	if h not in seen:
		seen[h] = []

	seen[h].append(a)

	if len(seen[h]) >= 3: # we can stop here, we've got all the data we need
		start = seen[h][1]
		end = seen[h][2]
		period = end - start
		break

first = waterlines[start]
second = waterlines[end] - waterlines[start]
last = waterlines[start + (targ - start) % period] - waterlines[start]
final = first + second * ((targ - start) // period) + last

print(first, second, (targ - 1) // period, last, final)
