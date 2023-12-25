from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]

c = 0

for r in range(2):
	f = [[f[x][y] + 1 for y in range(10)] for x in range(10)]

	def recurse(f):
		state = str(f)
		
		get_adjacent = lambda x, y: [[f[i][j] in range(10, 1337) for j in range(y - 1, y + 2) if i in range(10) and j in range(10)] for i in range(x - 1, x + 2)]
		f = [[f[x][y] + sum(chain(*get_adjacent(x, y))) for y in range(10)] for x in range(10)]

		f = [[1337 if f[x][y] > 9 else f[x][y] for y in range(10)] for x in range(10)]

		return f if str(f) == state else recurse(f)

	f = recurse(f)

	for y in range(10):
		for x in range(10):
			if f[x][y] > 9:
				c += 1
				f[x][y] = 0

print(c)
