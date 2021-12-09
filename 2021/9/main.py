f = [x for x in map(str.strip, open(0).read().strip().split('\n'))]

basins = []

def recurse(f, d, x, y):
	d.append((x, y))
	spot = int(f[x][y])

	def check(spot, d, f, x, y):
		return recurse(f, d, x, y) if x in range(len(f)) and y in range(len(f[x])) and spot < int(f[x][y]) < 9 and (x, y) not in d else 0

	return 1 + sum(map(lambda p: check(spot, d, f, *p), ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))))

for x in range(len(f)):
	for y in range(len(f[x])):
		spot = int(f[x][y])

		adjacent = []

		if x + 1 < len(f):    adjacent.append(int(f[x + 1][y]))
		if x - 1 >= 0:        adjacent.append(int(f[x - 1][y]))
		if y + 1 < len(f[x]): adjacent.append(int(f[x][y + 1]))
		if y - 1 >= 0:        adjacent.append(int(f[x][y - 1]))

		if any(spot < a for a in adjacent):
			d = []
			basins.append(recurse(f, d, x, y))

from functools import reduce
print(reduce(lambda x, y: x * y, sorted(basins)[-3:]))
