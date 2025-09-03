*f, = map(list, open(0).read().strip().split("\n"))
walls_orig = set()
start = None
end = None

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			walls_orig.add((i, j))
		elif f[i][j] == "S":
			start = (i, j)
		elif f[i][j] == "E":
			end = (i, j)

def fastest(walls):
	assert start is not None and end is not None

	q = [start]
	dist = [[float("inf")] * len(f) for _ in range(len(f))]
	dist[start[1]][start[0]] = 0

	while q:
		cx, cy = q.pop(0)

		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nx, ny = cx + dx, cy + dy

			if 0 <= nx < len(f) and 0 <= ny < len(f) and (nx, ny) not in walls:
				if dist[cy][cx] + 1 < dist[ny][nx]:
					dist[ny][nx] = dist[cy][cx] + 1
					q.append((nx, ny))

	return dist[end[1]][end[0]]

orig_time = fastest(walls_orig)
s = 0

for i, wall in enumerate(walls_orig):
	print(i, len(walls_orig))
	walls = walls_orig - {wall}
	if orig_time - fastest(walls) >= 100:
		s += 1

print(s)
