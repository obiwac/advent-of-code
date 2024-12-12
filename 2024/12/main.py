*f, = map(list, open(0).read().strip().split("\n"))
types = set()

for i in range(len(f)):
	for j in range(len(f[0])):
		types.add(f[i][j])

visited = [[False for _ in range(len(f[0]))] for _ in range(len(f))]
s = 0

for i in range(len(f)):
	for j in range(len(f[0])):
		if visited[i][j]:
			continue

		# BFS

		q = [(i, j, -1)]
		area = 0
		sides = {}

		while 1:
			if not q:
				break

			ii, jj, side = q.pop(0)

			if ii < 0 or jj < 0 or ii >= len(f) or jj >= len(f[0]) or f[ii][jj] != f[i][j]:
				if side <= 1:
					if (side, ii) not in sides:
						sides[(side, ii)] = set()

					sides[(side, ii)].add(jj)

				if side >= 2:
					if (side, jj) not in sides:
						sides[(side, jj)] = set()

					sides[(side, jj)].add(ii)

				continue

			if visited[ii][jj]:
				continue

			area += 1
			visited[ii][jj] = True

			q.append((ii + 1, jj, 0))
			q.append((ii - 1, jj, 1))
			q.append((ii, jj + 1, 2))
			q.append((ii, jj - 1, 3))

		side_count = 0

		for side in sides:
			*a, = sorted(sides[side])
			prev = -2

			for k in a:
				if k > prev + 1:
					side_count += 1

				prev = k

		print("Type", f[i][j], ":", area, "cells,", side_count, "sides")
		s += area * side_count

print(s)
