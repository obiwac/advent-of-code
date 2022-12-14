import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

PART = 2

f = open(0).read().strip().split('\n')
lines = []
m = [['.' for _ in range(1000)] for _ in range(500)]

floor = 0

for l in f:
	l = l.split(' -> ')
	r = l.pop()
	prev = tuple(map(int, r.split(',')))

	while l:
		r = l.pop()
		coord = tuple(map(int, r.split(',')))

		floor = max(floor, coord[1] + 2)

		for y in range(min(prev[1], coord[1]), max(prev[1], coord[1]) + 1):
			for x in range(min(prev[0], coord[0]), max(prev[0], coord[0]) + 1):
				m[y][x] = '#'

		lines.append((prev, coord))
		prev = coord

for i in range((PART == 2) * len(m[0])):
	m[floor][i] = '#'

def show(m):
	for l in m[0: 15]:
		print(''.join(l[470: 530]))

src = (500, 0)
stable = False
s = 0

while not stable:
	x, y = src

	while 1:
		try:
			while m[y + 1][x] == '.': # fall straight down
				y += 1

		except IndexError:
			stable = True
			break

		if m[y + 1][x - 1] in '#o':
			if m[y + 1][x + 1] in '#o':
				if PART == 2 and (x, y) == src: stable = True
				m[y][x] = 'o'
				s += 1
				break

			y += 1
			x += 1
			continue

		y += 1
		x -= 1

print(s)
exit(0)
