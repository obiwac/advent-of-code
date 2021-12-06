from itertools import accumulate as accum
from itertools import chain
from functools import reduce
from collections import Counter

f = [int(x) for x in map(str.strip, open(0).read().split(','))]
f = Counter(f)

for i in range(10):
	f.setdefault(i, 0)

for d in range(256 + 1):
	f[7] += f[0]
	f[9] += f[0]

	for i in range(10):
		f[i] = f[i + 1]

print(sum([f[x] for x in range(8)]))
