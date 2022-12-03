import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

f = open(0).read().strip().split('\n')

# part 1

s = 0

for r in f:
	m = len(r) // 2
	comp1 = set(r[:m])
	comp2 = set(r[m:])

	common, = comp1 & comp2
	common = ord(common)

	if ord('a') <= common <= ord('z'):
		s += common - ord('a') + 1

	else:
		s += common - ord('A') + 27

print(s)

# part 2

s = 0

for i in range(0, len(f), 3):
	a = f[i: i + 3]
	curr = set(a[0])

	for r in a:
		curr &= set(r)

	common ,= curr
	common = ord(common)

	if ord('a') <= common <= ord('z'):
		s += common - ord('a') + 1

	else:
		s += common - ord('A') + 27

print(s)

import time
time.sleep(1)
