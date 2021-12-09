f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]
from functools import reduce

POSITIONS = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def recurse(f, x, y):
	return {(x, y)} | reduce(lambda a, b: a | b, [({(x,y)}|recurse(f,z,w)if z in range(len(f))and w in range(len(f[x]))and f[x][y]<f[z][w]<9else set())for z,w in POSITIONS(x, y)])

from itertools import chain
from operator import mul

o = reduce(mul,sorted(chain(*[[len(recurse(f, x, y)) for y in range(len(f[x])) if any(f[x][y] < f[z][w] for z, w in POSITIONS(x, y) if z in range(len(f)) and w in range(len(f[x])))] for x in range(len(f))]))[-3:])

print(o)
