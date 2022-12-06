import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

import numpy as np

f = open(0).read().strip()

# part 1

n = 4

for i in range(len(f) - n + 1):
	if len(set(f[i: i + n])) == n:
		print(i + n)
		break

# part 2

n = 14

for i in range(len(f) - n + 1):
	if len(set(f[i: i + n])) == n:
		print(i + n)
		break
