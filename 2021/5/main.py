from itertools import accumulate
from functools import reduce
from itertools import chain

f = [[[int(z.strip()) for z in y.split(',')] for y in x.split('->')] for x in map(str.strip, open(0).readlines())]
# print(f)

c = {}

for l in f:
	def r(c,x,y,z,w,a,b):
		c[(x, y)] = c.get((x, y), 0) + 1
		return r(c,x+a,y+b,z,w,a,b)if x!=z or y!=w else c

	(lambda x,y,z,w:r(c,x,y,z,w,(z>x)-(z<x),(w>y)-(w<y)))(*chain(*l))

cnt = sum([x>1for x in c.values()])
print(cnt)