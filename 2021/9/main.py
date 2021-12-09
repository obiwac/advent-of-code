f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]

basins = []
POSITIONS = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def recurse(f, d, x, y):
	d.append((x, y))

	def check(spot, d, f, x, y):
		return recurse(f, d, x, y) if x in range(len(f)) and y in range(len(f[x])) and spot < f[x][y] < 9 and (x, y) not in d else 0

	return 1 + sum(map(lambda p: check(f[x][y], d, f, *p), POSITIONS(x, y)))

for x in range(len(f)):
	for y in range(len(f[x])):
		if any(f[x][y] < f[z][w] for z, w in POSITIONS(x, y) if z in range(len(f)) and w in range(len(f[x]))):
			basins.append(recurse(f, [], x, y))

from functools import reduce
print(reduce(lambda x, y: x * y, sorted(basins)[-3:]))
