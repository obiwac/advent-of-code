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
	a, b = l.split()

	opponent = ord(a) - ord('A') + 1
	mine     = ord(b) - ord('X') + 1

	s += mine

	if mine ==  opponent:          s += 3
	if mine == (opponent % 3) + 1: s += 6

print(s)
print(sum((lambda a,b:b-87+3*(a+23==b)+6*(b-88==(a-64)%3))(*map(ord,l.split()))for l in f))

# part 2

s = 0

for l in f:
	a, b = l.split()

	opponent = ord(a) - ord('A') + 1
	mine     = ord(b) - ord('X') + 1

	if mine == 2: s += 3 + opponent
	if mine == 3: s += 6

	if mine == 1: s += ((opponent + 1) % 3) + 1
	if mine == 3: s += (opponent % 3) + 1

print(s)
print(sum((lambda a,b:((a-63)%3+1,a-61,((a-64)%3)+7)[b-88])(*map(ord,l.split()))for l in f))
