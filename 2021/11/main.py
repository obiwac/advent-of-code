from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]

c = 0

while 1:
	for y in range(10):
		for x in range(10):
			f[x][y] += 1
	
	for p in range(30):
		for y in range(10):
			for x in range(10):
				if x not in range(10) or y not in range(10):
					continue
				
				if f[x][y] > 9 and f[x][y] < 1337:
					for i in range(x - 1, x + 2):
						for j in range(y - 1, y + 2):
							if i not in range(10) or j not in range(10):
								continue
							
							f[i][j] += 1
					
					f[x][y] = 1337 # don't reflash

	flashes = 0

	for y in range(10):
		for x in range(10):
			if f[x][y] > 9:
				flashes += 1
				f[x][y] = 0
	
	c += 1

	if flashes == 100:
		break

print(c)