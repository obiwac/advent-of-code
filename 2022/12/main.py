import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np

f = open(0).read().strip().split('\n')

start = (0, 0)
end = (0, 0)

heightmap = []

for i, l in enumerate(f):
	heightmap.append(list(map(ord, l)))

	for j, c in enumerate(l):
		if c == 'S':
			start = (j, i)
			heightmap[i][j] = ord('a')
		if c == 'E':
			end = (j, i)
			heightmap[i][j] = ord('z')

# Dijkstra

candidates = []

for j in range(len(heightmap))[::-1]:
	start = (0, j)
	q = []
	costs = [[np.inf] * len(heightmap[0]) for _ in heightmap]
	costs[start[1]][start[0]] = 0
	q.append((start, 0))

	while q:
		node, cost = q.pop()
		x, y = node
		incidents = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

		for i in incidents:
			if i[1] not in range(len(heightmap)) or i[0] not in range(len(heightmap[0])):
				continue

			if heightmap[i[1]][i[0]] > heightmap[y][x] + 1:
				continue

			if cost + 1 < costs[i[1]][i[0]]:
				costs[i[1]][i[0]] = cost + 1
				q.append((i, costs[i[1]][i[0]]))

	print(j, costs[end[1]][end[0]])
	candidates.append(costs[end[1]][end[0]])

print(min(candidates))
