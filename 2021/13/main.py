from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

a, b = open(0).read().strip().split("\n\n")

a = [*map(lambda x: [*map(int, x.split(','))], a.split('\n'))]
b = [*map(lambda x: [x.split('=')[0][-1], int(x.split('=')[1])], b.split('\n'))]

for f in b:
	# fold

	if f[0] == 'y':
		for i in a:
			if i[1] > f[1]:
				i[1] = f[1] - (i[1] - f[1])
	
	if f[0] == 'x':
		for i in a:
			if i[0] > f[1]:
				i[0] = f[1] - (i[0] - f[1])

a = set(map(tuple, a))

for y in range(6):
	for x in range(50):
		print(' █'[(x, y) in a], end = '')
	
	print()

print(len(a))