from matplotlib import pyplot as plt
import numpy as np

*f, = map(list, open(0).read().strip().split('\n'))
w, h = len(f[0]), len(f)

starting_point = (0, 0)

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == 'S':
			starting_point = (j, i)

vx = []
v = []

for steps in range(1, 100):
	vx.append(steps)
	q = [(starting_point, 0)]
	right_dist = set()
	pcurdist = -1

	while q:
		cur, cur_dist = q.pop(0)

		if pcurdist != cur_dist:
			q = list(set(q))
			pcurdist = cur_dist

		if cur_dist >= steps:
			continue

		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			x, y = cur[0] + dx, cur[1] + dy

			if f[y % h][x % w] in ".S":
				q.append(((x, y), cur_dist + 1))

				if cur_dist + 1 == steps:
					right_dist.add((x, y))

	print(steps, len(right_dist))
	v.append(len(right_dist))

"""
for j in range(len(f)):
	for i in range(len(f[j])):
		if f[j][i] == "." or f[j][i] == "S": print("O" if (i, j) in right_dist else ".", end="")
		if f[j][i] == "#": print("#", end="")

	print()
"""

p = np.polyfit(vx, v, 2)
x = 26501365

print(p[0] * x ** 2 + p[1] * x + p[2])

plt.plot(v)
plt.show()
