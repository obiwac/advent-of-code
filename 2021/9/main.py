f = [x for x in map(str.strip, open(0).read().strip().split('\n'))]

basins = []

def recurse(f, d, x, y):
	d.append((x, y))
	spot = int(f[x][y])
	adjacent = []

	def check(spot, adjacent, d, f, x, y):
		if x not in range(len(f)) or y not in range(len(f[x])):
			return 0
		
		a = int(f[x][y])
		return recurse(f, d, x, y) if spot < a and (x, y) not in d and a != 9 else 0

	positions = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
	return 1 + sum(map(lambda p: check(spot, adjacent, d, f, *p), positions))

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