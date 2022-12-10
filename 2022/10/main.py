import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np

f = open(0).read().strip().split('\n')

crt = [['.'] * 40 for _ in range(6)]
crt_i = 0

x = 1
cycle = 1
s = 0

i = [20, 60, 100, 140, 180, 220]

for l in f:
	a = l.split()
	p = x

	if a[0] == "addx":
		x += int(a[1])
		cycle += 2

	else:
		cycle += 1

	inside = cycle - 1

	if cycle in i or (a[0] == "addx" and inside in i):
		strength = inside * p if a[0] == "addx" and inside in i else cycle * x
		s += strength

	# crt

	if a[0] == "addx":
		crt_i += 1
		if crt_i % 40 in range(p - 1, p + 2): crt[crt_i // 40][crt_i % 40] = '#'
		crt_i += 1
		if crt_i % 40 in range(x - 1, x + 2): crt[crt_i // 40][crt_i % 40] = '#'
	
	else:
		crt_i += 1
		if crt_i % 40 in range(x - 1, x + 2): crt[crt_i // 40][crt_i % 40] = '#'

__import__("time").sleep(0.1)
print(s)

print("\n".join(map("".join, crt)))
