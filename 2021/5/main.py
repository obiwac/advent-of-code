from itertools import accumulate
from functools import reduce

f = [[[int(z.strip()) for z in y.split(',')] for y in x.split('->')] for x in map(str.strip, open(0).readlines())]
# print(f)

c = {}

for line in f:
	(x, y), (z, w) = line

	a = (z>x)-(z<x)
	b = (w>y)-(w<y)

	def recurse(c,x,y,z,w,a,b):
		c[(x, y)] = c.get((x, y), 0) + 1 # not super functional
		return recurse(c,x+a,y+b,z,w,a,b)if x!=z or y!=w else c

	recurse(c, x, y, z, w, a, b)

cnt = sum([x>1for x in c.values()])
print(cnt)