from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = [[*map(int, x.split('..'))] for x in map(str.strip, open(0).read().strip().replace("target area: x=", "").replace("y=", "").split(', '))]

count = 0
maxyl = []

px = []
py = []

for _vy in range(-200, 400):
	y = 0
	vy = _vy

	maxy = -9999

	for _ in range(300):
		y += vy
		maxy = max(y, maxy)

		vy -= 1

		if y in range(f[1][0], f[1][1] + 1):
			py.append(_vy)
			maxyl.append(maxy)
			break


for _vx in range(0, 300):
	x = 0
	vx = _vx

	for _ in range(300):
		x += vx

		if vx < 0:
			vx += 1
		
		if vx > 0:
			vx -= 1
		
		if x in range(f[0][0], f[0][1] + 1):
			px.append(_vx)
			break

print("proc...", len(px), len(py), len(px) * len(py))

for _vy in py:
	for _vx in px:
		x, y = (0, 0)
		vx, vy = (_vx, _vy)

		for _ in range(400):
			y += vy
			maxy = max(y, maxy)
			vy -= 1

			x += vx

			if vx < 0:
				vx += 1
			
			if vx > 0:
				vx -= 1

			if y in range(f[1][0], f[1][1] + 1) and x in range(f[0][0], f[0][1] + 1):
				count += 1
				break

print(max(maxyl))
print(count)