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

		q = [(i, j)]
		area = 0
		perimiter = 0

		while 1:
			if not q:
				break

			ii, jj = q.pop(0)

			if ii < 0 or jj < 0 or ii >= len(f) or jj >= len(f[0]):
				perimiter += 1
				continue

			if f[ii][jj] != f[i][j]:
				perimiter += 1
				continue

			if visited[ii][jj]:
				continue

			area += 1
			visited[ii][jj] = True

			q.append((ii + 1, jj))
			q.append((ii - 1, jj))
			q.append((ii, jj + 1))
			q.append((ii, jj - 1))

		print("Type", f[i][j], ":", area, "cells, perimiter", perimiter)
		s += area * perimiter

print(s)
