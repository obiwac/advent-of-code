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

m = [["."] * 7 for _ in range(200000)]
waterline = 0

def pm(m, h = waterline):
	print("===")
	for l in map("".join, reversed(m[h - 10: h + 10])):
		print(l)

a = 0
fi = 0
lcm = math.lcm(len(f), len(shapes))
waterlines = [0] # should be 2 * lcm large (adding 0 so we can index from 1)
targ = lcm * 4
seen = {} # k: hash, 

while 1:
	shape = shapes[a % len(shapes)].split('\n')
	x, y = 2, waterline + 3

	# simulate falling

	while 1:
		# fall

		y -= 1

		# push

		o = x
		c = f[fi % len(f)]
		fi += 1
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
	# if a == lcm * 2 or a == targ: break
	if a == targ: break

print(waterlines[targ]) # REMME

if 1: # targ > lcm * 2:
	first = waterlines[lcm]
	second = waterlines[lcm * 2] - waterlines[lcm]
	last = waterlines[lcm + targ % lcm] - waterlines[lcm]
	final = first + second * (targ // lcm - 1) + last

	print(first, second, last, final)

else:
	print(waterlines[targ])

__import__("time").sleep(0.1)
