f = [[*map(int, map(str.strip, x.split(',')))] for x in map(str.strip, open(0).read().strip().split('\n'))]

from itertools import accumulate

for y in f:
	print([*accumulate(y * 5)])

# print(sum(sum(f, [])))