import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

import numpy as np

f = open(0).read().strip().split('\n')

v = len(f) * 2 + (len(f[0]) - 2) * 2

candidates = set()

for y in range(len(f)):
	m = -1

	for x in range(len(f[y])):
		t = int(f[y][x])

		if t > m:
			m = t
			candidates.add((y, x, t))

	m = -1
	
	for x in range(len(f[y]) - 1, -1, -1):
		t = int(f[y][x])
		
		if t > m:
			m = t
			candidates.add((y, x, t))

for x in range(len(f[0])):
	m = -1

	for y in range(len(f)):
		t = int(f[y][x])
		
		if t > m:
			m = t
			candidates.add((y, x, t))

	m = -1
	
	for y in range(len(f) - 1, -1, -1):
		t = int(f[y][x])
		
		if t > m:
			m = t
			candidates.add((y, x, t))

print(len(candidates))

# find best scenic score

best = []

for y, x, t in candidates:
	if x == 0 or x == len(f[0]) or y == 0 or y == len(f):
		continue

	d = 0

	for i in range(y - 1, -1, -1):
		d += 1

		if int(f[i][x]) >= t:
			break
	
	score = d

	d = 0

	for i in range(y + 1, len(f)):
		d += 1

		if int(f[i][x]) >= t:
			break
	
	score *= d

	d = 0

	for i in range(x - 1, -1, -1):
		d += 1

		if int(f[y][i]) >= t:
			break

	score *= d

	d = 0

	for i in range(x + 1, len(f[0])):
		d += 1

		if int(f[y][i]) >= t:
			break

	score *= d
	best.append(score)

print(max(best))
