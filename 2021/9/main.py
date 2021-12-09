f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]
from functools import reduce

basins = []
POSITIONS = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def recurse(f, d, x, y):
	def check(spot, d, f, x, y):
		return d | ({(x, y)} | recurse(f, d, x, y) if x in range(len(f)) and y in range(len(f[x])) and spot < f[x][y] < 9 else set())

	return d | {(x, y)} | reduce(lambda a, b: a | b, map(lambda p: check(f[x][y], set(), f, *p), POSITIONS(x, y)))

for x in range(len(f)):
	for y in range(len(f[x])):
		if any(f[x][y] < f[z][w] for z, w in POSITIONS(x, y) if z in range(len(f)) and w in range(len(f[x]))):
			basins.append(len(recurse(f, set(), x, y)))

print(reduce(lambda x, y: x * y, sorted(basins)[-3:]))
