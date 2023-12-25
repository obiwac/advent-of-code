import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

*f, = map(list, open(0).read().strip().split('\n'))
e = set()

for y in range(len(f)):
	for x in range(len(f[0])):
		if f[y][x] == '#':
			e.add((y, x))

directions = [
		lambda y, x: ((y - 1, x), (y - 1, x - 1), (y - 1, x + 1)), # north
		lambda y, x: ((y + 1, x), (y + 1, x - 1), (y + 1, x + 1)), # south
		lambda y, x: ((y, x - 1), (y - 1, x - 1), (y + 1, x - 1)), # west
		lambda y, x: ((y, x + 1), (y - 1, x + 1), (y + 1, x + 1)), # east
]

prev = 0

for i in range(10000000):
	print("round", i)
	proposals = []

	for y, x in e:
		if \
			(y - 1, x) not in e and (y + 1, x) not in e and (y, x - 1) not in e and (y, x + 1) not in e and (y + 1, x + 1) not in e and \
			(y - 1, x - 1) not in e and (y + 1, x - 1) not in e and (y - 1, x + 1) not in e:
			continue

		for d in directions:
			a, b, c = d(y, x)

			if a not in e and b not in e and c not in e:
				proposals.append(((y, x), a))
				break

	props = [*map(lambda x: x[1], proposals)]

	for elf, want in proposals:
		# is proposal exclusive?

		if props.count(want) == 1:
			e.remove(elf)
			e.add(want)

	# print("===========", directions[0](0, 0))
	directions = directions[1:] + directions[:1]

	# for y in range(-10, 20):
	# 	for x in range(-10, 20):
	# 		print('#' if (y, x) in e else '.', end='')

	# 	print()

	#if i == 9: break
	#continue
	ha = hash(frozenset(e))

	if ha == prev:
		break

	prev = ha
	continue

minx = 999999
maxx = -999999
miny = 999999
maxy = -999999

for x, y in e:
	minx = min(minx, x)
	miny = min(miny, y)
	maxx = max(maxx, x)
	maxy = max(maxy, y)

print(i, (maxx - minx + 1) * (maxy - miny + 1) - len(e))
