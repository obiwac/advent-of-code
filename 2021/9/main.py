f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]
from functools import reduce

POSITIONS = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def recurse(f, x, y):
	def check(spot, f, x, y):
		return {(x, y)} | recurse(f, x, y) if x in range(len(f)) and y in range(len(f[x])) and spot < f[x][y] < 9 else set()

	return {(x, y)} | reduce(lambda a, b: a | b, map(lambda p: check(f[x][y], f, *p), POSITIONS(x, y)))

from itertools import chain

basins = [*chain(*[[len(recurse(f, x, y)) for y in range(len(f[x])) if any(f[x][y] < f[z][w] for z, w in POSITIONS(x, y) if z in range(len(f)) and w in range(len(f[x])))] for x in range(len(f))])]
print(reduce(lambda x, y: x * y, sorted(basins)[-3:]))
