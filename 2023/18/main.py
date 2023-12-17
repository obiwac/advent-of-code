import numpy as np

*f, = map(str, open(0).read().strip().split('\n'))

for p2 in (False, True):
	DIRS = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
	cx, cy = 0, 0
	x, y = [], []
	acc = 0

	for r in f:
		d, l, c = r.split()
		l = int(l)

		if p2:
			l = int(c[2: 7], 16)
			d = list(DIRS.keys())[int(c[-2])]

		dx, dy = DIRS[d]
		x.append(cx)
		y.append(cy)
		cx += dx * l
		cy += dy * l
		acc += l

	x = np.array(x)
	y = np.array(y)
	i = np.arange(len(x))

	shoelace = abs(np.sum(x[i - 1] * y[i] - x[i] * y[i - 1])) // 2
	print(shoelace + acc // 2 + 1)
