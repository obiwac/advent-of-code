from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = [list(x) for x in map(str.strip, open(0).read().strip().split('\n'))]
print(f)

W = len(f[0])
H = len(f)

def ix(x, y):
	if x < 0: x = W - 1
	if x >= W: x = 0

	if y < 0: y = H - 1
	if y >= H: y = 0

	return (x, y)

def get(f, x, y):
	x, y = ix(x, y)
	return f[y][x]

def set_(f, x, y, val):
	x, y = ix(x, y)
	f[y][x] = val

from copy import deepcopy

def step():
	global f
	n = [[f[y][x] for x in range(W)] for y in range(H)]

	# east facing

	for x in range(W)[::-1]:
		for y in range(H)[::-1]:
			if get(f, x, y) == '>' and get(f, x + 1, y) == '.':
				set_(n, x, y, '.')
				set_(n, x + 1, y, '>')

	# south facing

	f = deepcopy(n)

	for x in range(W)[::-1]:
		for y in range(H)[::-1]:
			if get(f, x, y) == 'v' and get(f, x, y + 1) == '.':
				set_(n, x, y, '.')
				set_(n, x, y + 1, 'v')

	f = n

def prt(f):
	print("===")

	for l in f:
		print("".join(l))

# prt(f)
# step()
# prt(f)
# step()
# prt(f)
# step()
# prt(f)
# step()
# prt(f)
# step()
# prt(f)
# step()
# prt(f)

c = 0

while 1:
	h = str(f)
	step()
	c += 1
	print("step", c)
	if h == str(f):
		break

c = 0

while 1:
	h = str(f)
	step()
	c += 1
	print("step", c)
	if h == str(f):
		break

print(c)
# print(h)
