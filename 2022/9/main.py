import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np

f = open(0).read().strip().split('\n')

head = [0, 0]
tails = [[0, 0] for _ in range(9)]

visited = set()

def show(head, tails):
	for y in range(10, -10, -1):
		s = ""
		for x in range(-10, 10):
			t = 0
			for i, tail in enumerate(tails):
				if (x, y) == tuple(tail):
					s += str(i + 1)
					t = 1
					break

			if (x, y) == tuple(head): s += "H"
			elif t: ...
			else: s += "."
		print(s)
	print("===", head, tail)

def d(a, b, c): # move diag
	if a[0] < b[0] and a[1] < b[1]:
		a[0] += 1
		a[1] += 1
	elif a[0] > b[0] and a[1] < b[1]:
		a[0] -= 1
		a[1] += 1
	elif a[0] < b[0] and a[1] > b[1]:
		a[0] += 1
		a[1] -= 1
	elif a[0] > b[0] and a[1] > b[1]:
		a[0] -= 1
		a[1] -= 1
	elif a[0] < b[0]: a[0] += 1
	elif a[0] > b[0]: a[0] -= 1
	elif a[1] < b[1]: a[1] += 1
	elif a[1] > b[1]: a[1] -= 1

for l in f:
	a, b = l.split()
	b = int(b)

	for i in range(b):
		prev = list(head)

		if a == 'U': head[1] += 1
		if a == 'D': head[1] -= 1
		if a == 'R': head[0] += 1
		if a == 'L': head[0] -= 1

		tp = deepcopy(tails)

		for i, tail in enumerate(tails):
			p = head if i == 0 else tails[i - 1]
			r = prev if i == 0 else tp[i - 1]

			if tail[0] < p[0] - 1: d(tail, p, r)
			if tail[0] > p[0] + 1: d(tail, p, r)
			if tail[1] < p[1] - 1: d(tail, p, r)
			if tail[1] > p[1] + 1: d(tail, p, r)

		visited.add(tuple(tails[-1]))

print(len(visited))
