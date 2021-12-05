from itertools import accumulate
from functools import reduce

f = [[[int(z.strip()) for z in y.split(',')] for y in x.split('->')] for x in map(str.strip, open(0).readlines())]
# print(f)

c = {}

for line in f:
	(x, y), (z, w) = line

	a = (z>x)-(z<x)
	b = (w>y)-(w<y)

	while x != z+a or y != w+b:
		c[(x, y)] = c.get((x, y), 0) + 1
		x+=a
		y+=b

cnt = sum([x>1for x in c.values()])
print(cnt)