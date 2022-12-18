import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

import sys
sys.setrecursionlimit(10000)

f = open(0).read().strip().split('\n')
field = {}

LAVA = 1
TRAPPED = 2
CHECKING = 3
FREE = 4

minx = +1000
maxx = -1000
miny = +1000
maxy = -1000
minz = +1000
maxz = -1000

for l in f:
	x, y, z = map(int, l.split(','))
	field[(x, y, z)] = LAVA

	minx = min(minx, x)
	maxx = max(maxx, x)
	miny = min(miny, y)
	maxy = max(maxy, y)
	minz = min(minz, z)
	maxz = max(maxz, z)

print(minx, miny, minz)
print(maxx, maxy, maxz)

faces = 0
PART = 1

def check(x, y, z):
	i = (x, y, z) in field

	if PART == 1:
		return not i

	if i and field[(x, y, z)] == CHECKING:
		return 2

	if i and field[(x, y, z)] == FREE:
		return 1

	# make sure this isn't a trapped air pocket

	if i and field[(x, y, z)] in (TRAPPED, LAVA):
		return 0

	if x < minx or x > maxx or y < miny or y > maxy or z < minz or z > maxz:
		return 1

	trapped = []
	field[(x, y, z)] = CHECKING

	trapped.append(check(x + 1, y, z))
	trapped.append(check(x - 1, y, z))
	trapped.append(check(x, y + 1, z))
	trapped.append(check(x, y - 1, z))
	trapped.append(check(x, y, z + 1))
	trapped.append(check(x, y, z - 1))

	del field[(x, y, z)]

	if trapped.count(0) == 6 - trapped.count(2):
		field[(x, y, z)] = TRAPPED
		return 0

	field[(x, y, z)] = FREE
	return 1

for cube in frozenset(field.keys()):
	x, y, z = cube

	faces += check(x + 1, y, z)
	faces += check(x - 1, y, z)
	faces += check(x, y + 1, z)
	faces += check(x, y - 1, z)
	faces += check(x, y, z + 1)
	faces += check(x, y, z - 1)

print(faces)
