from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = open(0).read().strip().split('\n\n')

a = f[0]
b = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in map(str.strip, f[1].split('\n'))}

z = {}

for j in range(len(a) - 1):
	x = a[j: j + 2]

	if x not in z:
		z[x] = 0

	z[x] += 1

for i in range(40):
	c = dict(z)
	z = {}

	for p in c:
		x = p[0] + b[p]
		y = b[p] + p[1]

		if x not in z:
			z[x] = 0
		
		z[x] += c[p]

		if y not in z:
			z[y] = 0
		
		z[y] += c[p]

elements = {}

for e in z:
	c = e[0]
	
	if c not in elements:
		elements[c] = 0
	
	elements[c] += 1 * z[e]

counter = Counter(elements)
print(counter.most_common()[0][1] - 1 - counter.most_common()[-1][1])
