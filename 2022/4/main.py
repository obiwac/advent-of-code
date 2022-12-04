import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

f = open(0).read().strip().split('\n')

# part 1

s = 0

for l in f:
	a = l.strip().split(',')
	x1, x2 = map(int, a[1].split('-'))
	y1, y2 = map(int, a[0].split('-'))

	if x1 >= y1 and x2 <= y2:
		s += 1

	elif y1 >= x1 and y2 <= x2:
		s += 1

print(s)

# part 2

s = 0

for l in f:
	a = l.strip().split(',')
	x1, x2 = map(int, a[1].split('-'))
	y1, y2 = map(int, a[0].split('-'))

	if y1 <= x1 <= y2:
		s += 1
	
	elif x1 <= y1 <= x2:
		s += 1

print(s)